
### 公式计算：

    注意：这里所有的准确率计算都是【排除了无法提取数字作为答案的情况】
    
    第一轮准确率 :第一轮准确率
    第二轮准确率: 第二轮准确率
    全面准确率:  只有两轮都正确才算做正确
    平均准确率：（第一轮答对的题数+第二轮答对的题数）/（第一轮总题数+第二轮总题数）
    
    准确率综合得分：0.5*全面准确率+0.5*平均准确率
    
    推理步数加权得分：
    1）分别计算推理步数1，2，3，4，5对应的模型平均得分avg_score_step_1, ..., avg_score_step_5；
    2）计算推理步数加权得分：（1*avg_score_step_1 + ...+ 5*avg_score_step_5）/(1+...+5)
    
    综合得分：0.5* 准确率综合得分+ 0.5 * 推理步数加权得分


#### 模型回复文件的示例字段的说明：
    一行记录：
    {"model_answer_turns_1": "答案是【24】",
     "answer": "88",
      "model_answer_turns_2": 
      "答案是【61】",
       "answer_followup": "73", 
       "reasoning_step_ref": "5", 
       "reasoning_step_followup_ref": "5"}
       
       字段说明：
       model_answer_turns_1：第一轮模型的回复
       answer：问题1的标准答案
       model_answer_turns_2：第二轮模型的回复
       answer_followup：问题2的标准答案
       reasoning_step_ref：第一问的参考的推理步数
       reasoning_step_followup_ref：第二问的参考的推理步数
       
       
