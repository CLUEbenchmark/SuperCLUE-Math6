import jsonlines
import regex as re

def unify_score(x,y):
    if y==0:
        return 0
    return round(x/y*100,2)


def score(path):
    # 第一轮，所有题的数量
    all_count_turns_1=0

    # 第二轮，所有题的数量
    all_count_turns_2=0

    # 第一轮和第二轮都获取到模型回复的数量
    count_turns_all=0

    # 第一轮，未获取到模型回复的数量
    unfinished_count_turns_1=0

    # 第二轮，未获取到模型回复的数量
    unfinished_count_turns_2=0

    # 第一轮，模型回答正确的数量
    win_count_turns_1=0

    # 第二轮，模型回答正确的数量
    win_count_turns_2=0

    # 两轮，模型都回答正确的数量
    win_count_turns_all=0

    # 用第一种方法团提取到模型答案数量
    processed_count_m1=0

    # 用第二种方法团提取到模型答案数量
    processed_count_m2=0

    # 第一轮未处理的数据量，包含未获取的模型回复，以及获取到了模型回复但是没有获取到标准数字答案

    unprocessed_turns_1=0

    # 第二轮未处理的数据量，包含未获取的模型回复，以及获取到了模型回复但是没有获取到标准数字答案
    unprocessed_turns_2=0

    # 每个reasoning step上模型的加权总分,{reasoning_step:score, }
    score_for_reasoning_step = {}

    # reasoning step对应的问题数量(reasoning_step:num_of_problems)
    sample_num_for_reasoning_step = {}

    for line in jsonlines.open(path):


        model_answer_turns_1=line.get(f'model_answer_turns_1',None)
        model_answer_turns_2=line.get(f'model_answer_turns_2',None)

        ref_answer_turns_1=line[f'answer']
        ref_answer_turns_2=line[f'answer_followup']
        reasoning_steps_turns_1 = line["reasoning_step_ref"]
        reasoning_steps_turns_2 = line["reasoning_step_followup_ref"]


        if not model_answer_turns_1:
            model_answer_turns_1=''
            unfinished_count_turns_1+=1
        if not model_answer_turns_2:
            model_answer_turns_2=''
            unfinished_count_turns_2+=1

        if model_answer_turns_1 and model_answer_turns_2:
            count_turns_all+=1

        obj_left_turns_1_m1=re.findall('【(\d+)】',model_answer_turns_1)
        obj_left_turns_1_m2=re.findall('(\d+)[^\d]*$',model_answer_turns_1)

        # +=2

        ans_left_1=''
        all_count_turns_1+=1

        
        if obj_left_turns_1_m1:
            ans_left_1=obj_left_turns_1_m1[0]
            processed_count_m1+=1
            sample_num_for_reasoning_step[reasoning_steps_turns_1] = sample_num_for_reasoning_step.get(reasoning_steps_turns_1, 0) + 1


        elif obj_left_turns_1_m2:
            ans_left_1=obj_left_turns_1_m2[0]
            processed_count_m2+=1
            sample_num_for_reasoning_step[reasoning_steps_turns_1] = sample_num_for_reasoning_step.get(reasoning_steps_turns_1, 0) + 1
        else:
            unprocessed_turns_1+=1

        obj_left_turns_2_m1=re.findall('【(\d+)】',model_answer_turns_2)
        obj_left_turns_2_m2=re.findall('(\d+)[^\d]*$',model_answer_turns_2)
        # obj_left_turns_1_m2=re.findall('(\d+)[^\d]*?$',model_answer_turns_1)

        ans_left_2=''
        all_count_turns_2+=1
        if obj_left_turns_2_m1:
            ans_left_2=obj_left_turns_2_m1[0]
            processed_count_m1+=1
            sample_num_for_reasoning_step[reasoning_steps_turns_2] = sample_num_for_reasoning_step.get(reasoning_steps_turns_2, 0) + 1

        elif obj_left_turns_2_m2:
            ans_left_2=obj_left_turns_2_m2[0]
            processed_count_m2+=1
            sample_num_for_reasoning_step[reasoning_steps_turns_2] = sample_num_for_reasoning_step.get(reasoning_steps_turns_2, 0) + 1
        else:
            unprocessed_turns_2+=1


        if ans_left_1==ref_answer_turns_1:
            win_count_turns_1+=1
            score_for_reasoning_step[reasoning_steps_turns_1] = score_for_reasoning_step.get(reasoning_steps_turns_1, 0) + 1
            
            
            

        if ans_left_2==ref_answer_turns_2:
            win_count_turns_2+=1
            score_for_reasoning_step[reasoning_steps_turns_2] = score_for_reasoning_step.get(reasoning_steps_turns_2, 0) + 1
           

        if ans_left_1==ref_answer_turns_1 and ans_left_2==ref_answer_turns_2:
            win_count_turns_all+=1

    # 计算reasoning step对应的平均分
    min_level = 1
    max_level = 5
    score_for_reasoning_step = {_:round(score_for_reasoning_step[str(_)]/sample_num_for_reasoning_step[str(_)], 2) for _ in range(min_level, max_level+1)}
    
        

    overall={}

    overall['第一轮准确率']=unify_score(win_count_turns_1,all_count_turns_1-unfinished_count_turns_1)
    overall['第二轮准确率']=unify_score(win_count_turns_2,all_count_turns_2-unfinished_count_turns_2)
    overall['严格准确率']=unify_score(win_count_turns_all,count_turns_all)
    overall['总体准确率']=unify_score(win_count_turns_1+win_count_turns_2,all_count_turns_1+all_count_turns_2-unfinished_count_turns_1-unfinished_count_turns_2)
    overall["推理步数-加权得分"] = unify_score(sum([int(step_num)*score_for_reasoning_step[step_num] for step_num in score_for_reasoning_step]), sum(range(min_level, max_level+1)))
    overall["综合分数"] = 0.5 *(0.5 * overall["总体准确率"]+0.5*overall["严格准确率"])+0.5*overall["推理步数-加权得分"]
    overall['获取到括号内作为答案数量']=processed_count_m1
    overall['获取到最后一个数字作为答案数量']=processed_count_m2
    overall['标准答案无法获取']=unprocessed_turns_1+unprocessed_turns_2-unfinished_count_turns_1-unfinished_count_turns_2
    overall['尚获取到模型回复']=unfinished_count_turns_1+unfinished_count_turns_2

    return overall

if __name__=="__main__":
    path = "your_answer_json_file_name.json"
    print(score(path))
