## SuperCLUE-Math6：新一代中文数学推理数据集的探索之旅

在人工智能领域，我们正见证着大语言模型如ChatGPT和GPT-4的蓬勃发展，它们是我们走向通用人工智能梦想的关键一步。中文大模型的推出，更是开启了人
工智能在各行各业的全新应用时代；像GSM8K数学推理任务，由于可以考察多步逻辑推理推能力、应用数学和实现知识的能力、需要自然语言理解和解决方案、
具备精确的评估标准的任务，受到了广泛的使用。然而，在这一进程中，缺乏能够测试中文大模型在数学推理上能力的原生数据集，导致中文模型的数学逻辑能力评估，
一直依赖于英文测试集。

为了缓解这一问题，我们推出了SuperCLUE-Math6数据集。这是一个GSM8K的中文升级版，专门设计来测试中文大模型在数学推理方面的核心能力。
SuperCLUE-Math6不仅延续了GSM8K的高质量和多样性，更在难度和应用广度上进行了适当的扩充。它的推出，旨在解决中文模型评估中的关键问题，并提供一个全面的测试平台。

    SuperCLUE-Math6具有四大特点：
    1. 中文原生场景的数学推理：每个问题均以中文原生环境呈现，配备详细的自然语言解题方案，强化了模型在本土语言环境下的适用性和实际应用价值。
    2. 多轮交互下的推理能力考察：适应真实交流，通过问题及其追问，考察模型在连续对话环境中的逻辑推理与问题解决能力。
    3. 推理能力等级自动评定：独创的评估系统能自动给出大模型处理数学问题的推理能力等级，为模型智力水平提供量化指标。
    4. 内容的丰富性和具体化：包含数百个场景，确保模型在多种情境下均能得到有效评估，提高了数据集的应用范围和实用性。
    SuperCLUE-Math的推出不仅填补了中文数学推理数据集的空缺，而且对于提升中文大模型在复杂逻辑和数学问题解决能力上的表现具有重要价值。
    
它的应用将加速人工智能在教育、金融分析和技术领域等的本土化进程，同时助力模型更贴近人类的思维方式，为实现真正的通用人工智能奠定坚实的基础。
期待SuperCLUE-Math能激励更多的创新，推动人工智能技术在各行各业的广泛应用，从而为社会带来更深远的影响。

官网地址：<a href='https://www.CLUEbenchmarks.com/superclue_math6.html'>https://www.CLUEbenchmarks.com/superclue_math6.html</a>

公众号推文地址：<a href="https://mp.weixin.qq.com/s/jM2rgWE_-2TC7c49e22jAw">https://mp.weixin.qq.com/s/jM2rgWE_-2TC7c49e22jAw</a>

申请地址 ：<a href='https://wj.qq.com/s2/11984326/86bb/'>https://wj.qq.com/s2/11984326/86bb/</a>

## SuperCLUE-Math6

### SC-Math6与GSM8K区别联系

| 序号 | 对比项目                       | SC-Math6 | GSM8K |
|:----:|:------------------------------:|:---------------:|:-----:|
|  1   | 数学逻辑推理                   |       YES       |  YES  |
|  2   | 自然语言解决方案               |       YES       |  YES  |
|  3   | 小学数学知识                   |       YES       |  YES  |
|  4   | 多步推理                       |       YES       |  YES  |
|  5   | 中文原生场景                   |       YES       |   NO  |
|  6   | 多轮深入推理                   |       YES       |   NO  |
|  7   | 题目推理步骤数                 |       YES       |   NO  |
|  8   | 可解析性的</br>模型推理等级   |       YES       |   NO  |
|  9   | 测试题数量                       | 2024题<br/>（1012对）| 1300题 |


###  推理步数的分布
| 推理步数 | 题目占比（%） |
|:--------:|:------------:|
|    1     |    15-20     |
|    2     |    15-20     |
|    3     |    45-50     |
|    4     |     5-10     |
|    5     |     5-10     |

### 推理等级的计算
我们介绍了一种创新的方案来评估大模型的推理能力。它通过结合模型在不同推理步骤的表现和总体准确率，以科学且公正的方式进行评估。
其特点在于简明易懂，通过合理的阈值设置，确保了性能相近的模型被归入同一等级，方便了对新模型的快速评级，而无需重新评估现有模型。
这提供了一个透明、易于理解的框架，帮助公众衡量和比较大模型的推理能力和智力水平。
#### 推理等级的计算方案
为了设计一个科学且综合的方案来计算模型的推理等级，我们可以采用以下步骤：
##### 1. 数据准备和处理
- 将提供的数据整理为一个表格，以便进行计算。
##### 2. 计算每个模型的推理步数得分
- 由于更长的推理步数更难，我们将为每个推理步数赋予不同的权重。步数1的权重为1，步数5的权重为5。
- 对每个模型，计算加权平均得分：

##### 3. 计算每个模型的综合得分
- 综合得分=0.5×推理步数得分+0.5×准确率得分
- 综合得分将由推理步数得分和准确率得分共同决定，每部分占50%的权重。
##### 4. 等级划分
- 根据综合得分进行等级划分，等级从1到5，等级5为最高，等级1为最低。
- 使用阈值（0.05分）来确定等级。如果两个模型的综合得分差距在0.05分以内，它们处于同一个等级。
##### 5. 新模型的等级计算
- 对于新模型，使用相同的方法计算其综合得分。
- 将其综合得分与现有模型的综合得分进行比较，按照相同的等级划分原则，确定其等级。

### 评估标准及Prompt
采取完全匹配的方式，计算准确率。
其中，答案只能是非负整数。

使用的Prompt:
<这里问题的内容>

---
注意：回答格式如下：“解题过程+'\n\n'+最终答案:【XXX】”。XXX，必须为非负整数，如35；解题过程中如涉及小数可保留两位数，最终结果如有小数四舍五入为非负整数。

###  模型列表及使用方式
|     模型名称      |   机构   | 使用方式 |
|:-----------------:|:--------:|:--------:|
| GPT_4_1106_Preview | OpenAI   |   API    |
|      GPT_4        | OpenAI   |   API    |
|   文心一言4.0    |  百度    |   API    |
| GPT_3.5_Turbo   | OpenAI   |   API    |
|  ChatGLM_Turbo    | 智谱AI   |   API    |
|  Qwen_14B_Chat    | 阿里云   |   API    |
| Baichuan2_13B_Chat | 百川智能 |   模型   |
|  ChatGLM3_6B      | 智谱AI   |   模型   |
|   讯飞星火_V3.0    | 科大讯飞  |   API    |
| 文心一言3.5 |  百度    |   模型   |
| Chinese_Alpaca2_13B | Yiming Cui | 模型 |


## 测评结果
### SuperCLUE推理能力等级
| 模型名称              | **推理<br/>等级** | 综合<br/>得分 | 推理步数<br/>加权得分 | 准确率<br/>综合得分 |
|:---------------------:|:--------:|:--------:|:------------:|:----------:|
| GPT_4_1106_Preview    |    **5级**     |  87.76   |     88.60     |   86.92    |
| GPT_4                 |    **5级**     |  83.86   |     83.60    |   84.12    |
| 文心一言4.0         |    **5级**     |  79.64   |     80.73    |   78.55    |
| GPT_35_Turbo       |    **4级**     |  53.75   |     54.87    |   52.64    |
| ChatGLM_Turbo         |    **4级**     |  52.55   |     53.60     |   51.49    |
| Qwen_14B_Chat         |    **4级**     |  49.05   |     49.73    |   48.37    |
| 讯飞星火_V3.0          |    **3级**     |  37.39   |     40.87    |   33.91    |
| Baichuan2_13B_Chat    |    **3级**     |  36.76   |     38.40     |   35.12    |
| ChatGLM3_6B           |    **3级**     |  33.03   |     34.13    |   31.92    |
| 文心一言3.5     |    **2级**     |  21.01   |     22.20     |   19.82    |
| Chinese_Alpaca2_13B  |    **2级**     |  18.09   |     18.67    |   17.51    |

###   模型准确率得分
|      模型名称       | **全面<br/>准确率** | 平均<br/>准确率 | 第一轮<br/>准确率 | 第二轮<br/>准确率 | 两轮<br/>差异 |
|:-------------------:|:----------:|:----------:|:------------:|:------------:|:----------------:|
| GPT_4_1106_Preview  |   83.68    |   90.16    |     94.22    |     86.10    |      -8.12       |
|        GPT_4        |   80.50    |   87.73    |     91.70    |     83.77    |      -7.93       |
|     文心一言4.0    |   73.32    |   83.77    |     89.74    |     77.80    |      -11.94      |
|   GPT_3.5_Turbo   |   43.94    |   61.33    |     72.48    |     50.19    |      -22.29      |
|    ChatGLM_Turbo    |   42.44    |   60.54    |     71.92    |     49.16    |      -22.76      |
|    Qwen_14B_Chat    |   38.54    |   58.19    |     72.31    |     44.06    |      -28.25      |
| Baichuan2_13B_Chat  |   25.09    |   45.15    |     59.24    |     31.06    |      -28.18      |
|     ChatGLM3_6B     |   21.23    |   42.60    |     56.72    |     28.44    |      -28.28      |
|     讯飞星火_V3.0     |   20.52    |   47.29    |     69.12    |     25.47    |      -43.65      |
| Chinese_Alpaca2_13B |   10.23    |   24.79    |     33.21    |     16.32    |      -16.89      |
| 文心一言3.5   |    9.51    |   30.13    |     43.00    |     17.26    |      -25.74      |


####  指令遵循率与回答长度

| 模型名称              | 指令遵循率<br/>（答案） | 回答<br/>长度 |
|:---------------------:|:------------------:|:------------:|
| GPT_4_1106_Preview    |       99.44        |    173.48    |
| GPT_4                 |       99.21        |    126.75    |
| 文心一言4.0          |       68.04        |    143.78    |
| GPT_3.5_Turbo       |       54.64        |     82.11    |
| ChatGLM_Turbo         |       60.15        |     91.84    |
| Qwen_14B_Chat         |       90.67        |     71.1     |
| Baichuan2_13B_Chat    |        1.54        |      70.00      |
| ChatGLM3_6B           |       20.91        |     56.29    |
| 讯飞星火_V3.0           |       53.66        |     61.03    |
| Chinese_Alpaca2_13B  |       18.15        |     46.50    |
| 文心一言3.5     |       64.68        |     43.14    |

###   推理步数的成绩分布
|     模型名称                |   步数1   |   步数2   |   步数3   |   步数4   |   步数5   |
|:-------------------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| GPT_4_1106_Preview  | 0.92  | 0.89  | 0.91  | 0.89  | 0.86  |
| GPT_4               | 0.92  | 0.91  | 0.89  | 0.82  | 0.77  |
| 文心一言4.0        | 0.87  | 0.85  | 0.85  | 0.81  | 0.75  |
| GPT_3.5_Turbo     | 0.73  | 0.65  | 0.61  | 0.48  | 0.49  |
| ChatGLM_Turbo       | 0.70  | 0.65  | 0.60  | 0.51  | 0.44  |
| Qwen_14B_Chat       | 0.72  | 0.58  | 0.60  | 0.47  | 0.38  |
| Baichuan2_13B_Chat  | 0.56  | 0.48  | 0.44  | 0.38  | 0.28  |
| ChatGLM3_6B         | 0.58  | 0.49  | 0.41  | 0.27  | 0.25  |
| 讯飞星火_V3.0          | 0.62  | 0.48  | 0.47  | 0.31  | 0.38  |
| 文心一言3.5  | 0.49  | 0.29  | 0.29  | 0.16  | 0.15  |
| Chinese_Alpaca2_13B| 0.40  | 0.29  | 0.22  | 0.14  | 0.12  |

###   成绩对比：SC-Math vs GSM8K
| 模型名称            | SC-Math6<br/>全面准确率 | GSM8K              | 成绩来源            |
|:-------------------:|:------------------:|:------------------:|:-------------------:|
| GPT_4_1106_Preview  |       83.68        |       未报告       |         --         |
| GPT_4               |       80.50        | 92.0<br/> (5-shot CoT)  |    GPT-4 report    |
| 文心一言4.0       |       73.32        |       未报告       |         --         |
| GPT_3.5_Turbo        |       43.94        | 57.1<br/> (5-shot)      |    GPT-4 report    |
| ChatGLM_Turbo       |       42.44        |       未报告       |         --         |
| Qwen_14B_Chat       |       38.54        | 50.3 <br/>(0-shot)      | Modelscope<br/>项目     |
| Baichuan2_13B_Chat  |       25.09        | 52.77<br/>(base)        | Baichuan2<br/>report   |
| ChatGLM3_6B         |       21.23        | 72.3<br/>(0-shot CoT)   | ChatGLM3-6B<br/>Github |
| 讯飞星火_V3.0          |       20.52        |       未报告       |         -          |
| Chinese_Alpaca2_13B|       10.23        |       未报告       |         -          |
| 文心一言3.5   |        9.51        |       未报告       |         -          |

## 测评结论

通过我们获得的推理等级数据，我们可以得出以下三个关键结论：

#### 1. 先进模型的卓越表现：
    顶级模型（如GPT_4_1106_Preview、GPT_4 和文心一言4.0 ）在推理任务中展现了卓越的性能，特别是在处理高难度的多步推理任务时。
    它们在推理能力和准确性方面均达到了较高的标准，证明了当前大模型的先进水平。
#### 2. 性能分层明显：
    通过对不同模型的综合评估，我们可以看到性能上的明显分层。高等级模型在复杂任务上的表现远远超过低等级模型，这反映了在大模型领域内技术和能力的多样性和分层。
#### 3. 针对不同需求的模型选择：
    不同等级的模型提供了根据具体应用场景和需求选择合适模型的依据。例如，对于需要高精度和复杂推理能力的任务，更适合选择等级较高的模型；
     而对于一些基础应用，则可以考虑使用等级较低但仍具有效率和准确性的模型。


通过分析准确率和指令遵循率得分情况，我们还可以看到：

#### 1. 准确率的递减趋势：
在所有模型中，第二轮准确率普遍低于第一轮准确率，这表明随着任务复杂度的增加（从第一轮到第二轮），模型的性能出现了下降。这种趋势在所有模型中普遍存在，
表明在设计和优化模型时，需要特别关注其在持续任务中的稳定性和适应性。

      比如，GPT_4_1106_Preview的第一轮准确率为94.22%，而第二轮准确率为86.10%，准确率下降了8.12%。同样地，ERNIE_35_Turbo_v2的第一轮准确率为43.00%，第二轮准确率为17.26%，下降了25.74%。
#### 2. GPT系列模型的卓越性能：
 GPT_4_1106_Preview和GPT_4在各项指标中均表现优异，尤其在全面准确率和平均准确率方面。这反映了GPT系列模型在处理复杂任务时的高效性和可靠性，
 同时也表明了其在语言理解和生成方面的先进性。
    GPT_4_1106_Preview在全面准确率上达到了83.68%，平均准确率为90.16%，而GPT_4的全面准确率为80.50%，平均准确率为87.73%，均高于其他模型。
#### 3. 指令遵循率与准确率的相关性：
高指令遵循率模型（如GPT_4_1106_Preview和GPT_4）通常也展现了较高的准确率，而低指令遵循率模型（如Baichuan2_13B_Chat）则准确率较低。
这表明指令遵循率可能是衡量模型整体性能的一个重要指标，尤其在评估模型对任务要求的理解和执行能力时。
     GPT_4_1106_Preview的指令遵循率为99.44%，全面准确率为83.68%，而Chinese_Alpaca2_13B的指令遵循率仅为18.15%，全面准确率也较低，仅为10.23%。
#### 4. 准确率与答案长度的潜在关系：
在某些模型（如GPT_4_1106_Preview）中，较高的准确率伴随着较长的平均答案长度，这可能暗示这些模型在生成详尽回答时更为精确。
然而，这一趋势并不在所有模型中一致出现，表明答案长度与准确率之间的关系可能受多种因素影响，包括模型的设计和训练数据。
      GPT_4_1106_Preview的平均答案长度为173.48，准确率较高，而ChatGLM3_6B的平均答案长度为56.29，准确率相对较低。这暗示在某些情况下，答案长度可能与准确率相关。
#### 5. 性能差异的可能原因：
观察各模型之间的性能差异，可能反映了它们在架构、训练数据集、优化策略等方面的不同。例如，GPT系列模型可能因为更大的模型规模、更广泛的训练数据或更高级的优化技术而表现更佳。
对这些差异的深入研究有助于理解和改进现有模型的性能。

## 示例
#### 示例1
<img src="https://github.com/CLUEbenchmark/SuperCLUE-Math6/blob/main/resources/img/example2.png"  width="86%" height="86%"></img>

#### 示例2
<img src="https://github.com/CLUEbenchmark/SuperCLUE-Math6/blob/main/resources/img/example0.png"  width="86%" height="86%"></img>

#### 示例3
<img src="https://github.com/CLUEbenchmark/SuperCLUE-Math6/blob/main/resources/img/example1.png"  width="86%" height="86%"></img>



## 讨论交流与使用

<p float="left"> 
  微信群：  
  <img src="https://github.com/CLUEbenchmark/SuperCLUE-Math6/blob/main/resources/img/scmath_group.jpeg"  width="30%" height="30%"></img>
  联系人：
  <img src="https://github.com/CLUEbenchmark/SuperCLUE-Math6/blob/main/resources/img/brightmart_s.jpeg"  width="30%" height="30%"></img>
</p> 



