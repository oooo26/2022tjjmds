## 主题

基于xxx模型的

粤港澳大湾区政策

对地区xxx的影响因子分析

—— 以xxx为例

## 数据

地区选取：

- 广州
- 香港/澳门（因为数据标准的问题，不一定很好处理）
- 其他广东地区？

参考[这篇](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2019&filename=TAJJ201908017&uniplatform=NZKPT&v=UEK75FlycaqtjBnGsJAlX_rQfmshO_3Gt6dWeWgvqeJq_d4ySKDMADg5bglXyZLf)，收集2015-2020年每个地区的数据：（尽量收集）

- 政策（断点）：有无大湾区政策

- 数据示例：
    - 科技
        - 研究经费
        - 研究经费在GDP中占比
        - 科技人才数量
        - 创新发明专利数量
        - 创新发明专利数量在总申请专利数量的占比
    - 经济
        - 人均GDP
        - 进出口
    - 产业
        - 就业人员中制造业人员占比
        - 地区生产总值中第三产业占比
        - 地区生产总值中高新技术产业占比
        - 地区内高新企业数量
    - 教育
        - 高校（大学）数量
        - 高校（大学）学生人数
        - 高校（大学）教职工人数
        - 教育经费
        - 教育经费支出占比
    - 社会
        - 移动电话普及率
        - 互联网用户数
    - 生态
        - 污水合格率
        - 空气质量平均指数、空气质量为优的天数占比
        - 人均绿地面积

方法（包含绘图）

- 指标处理：
    - 主成分
    - 层次分析法

- 变量处理：对每个大类数据单独分析，最后每类总结出两三项小指标
    - 相关性分析
    - 聚类，稀疏主成分
    - （待定）“是否实行某个政策”作为指标变量

- 主要模型：

    - [断点回归模型](https://www.jianshu.com/p/6ee94bcf2c29)：以“大湾区政策实行”作为断点，研究局部地区，参考[这篇](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD201601&filename=1015368383.nh&uniplatform=NZKPT&v=Zh5f2Kd1itAVV0LyDtEbCrMUm9M7P64Be0t3rWn0DQIgdCEsTGywUalYnFfKW55V)；
    - [空间自相关杜宾模型](https://zhuanlan.zhihu.com/p/432716121)：研究多地区相互影响，参考[这篇](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTODAY&filename=GJTA202202011&uniplatform=NZKPT&v=WL8niG7LIZ7Qsea97xBWOxZo96zWb05IybLHilzki2XpME_-pn43gwDdHzNXedDe)；

- 分析：

    - 通过变量参数分析重要性

    - 除了大湾区政策对经济的发展外，也要注意它对其他自变量的影响（断点回归）



## 文字描述

参考其他论文来吹

- 模型与研究方法
- 数据说明
    - 数据选取原则：统一性，可比性，代表性，可获得性，...
    - 数据来源
    - 每项数据的具体功能
- 提出发展方案



## 计划安排

- [ ] T1  （3 day）

    | 任务                          | 人员    | 备注                                                         |
    | ----------------------------- | ------- | ------------------------------------------------------------ |
    | 确认各项数据                  | A，B，C | 保证**多地区**的相同项数据都能获取；可以有少量缺失；如果有难以收集的项，尽量找相关的项替换 |
    | 按地区收集数据：整理成csv格式 | A, B，C | 每整理好一个地区，就发群上；缺失值可以用本地区的回归或插值补全（要记得是哪个值，可能会写进论文） |

- [ ] T2 （2 day）

    | 任务                                         | 人员 | 备注                   |
    | -------------------------------------------- | ---- | ---------------------- |
    | 确认层次分析法的流程，并写出文字描述         | A    |  |
    | 确认断点回归模型的流程，并写出文字描述       | B    |  |
    | 确认空间自相关杜宾模型的流程，并写出文字描述 | C    |  |

- [ ] T3 （2 day）

    | 任务                                     | 人员 | 备注                                                         |
    | ---------------------------------------- | ---- | ------------------------------------------------------------ |
    | 对指标进行层次分析                       | A    | 保证权重合理                                                 |
    | 对解释数据进行预处理，用不同方法提取变量 | B，C | 例如经验主义、聚类、稀疏主成分、因果分析等等；记录下可能出现的多重共线性、冗余变量等问题；每一类数据需要有两三个指标，比如聚类就需要两三个fold，并且需要相关性尽量低。 |

- [ ] T4 （2 day）

    | 任务                                                         | 人员 | 备注                         |
    | ------------------------------------------------------------ | ---- | ---------------------------- |
    | 补充解释数据和指标的文字描述，了解断点回归模型和空间自相关杜宾模型 | A    | ~~摸鱼~~为检查论文内容做准备 |
    | 在各个地区实现断点回归，记录初步结果                         | B    | 比较各种方法提取的变量       |
    | 实现空间自相关杜宾模型，记录初步结果                         | C    | 比较各种方法提取的变量       |


- [ ] T5 （2 day）
    | 任务                                         | 人员 | 备注                               |
    | -------------------------------------------- | ---- | ---------------------------------- |
    | 补充变量提取的文字描述                       | A    | 如果可以，给每个变量一个合适的名字 |
    | 在各个地区实现断点回归，文字描述、绘图、结果 | B    |                                    |
    | 实现空间自相关杜宾模型，文字描述、绘图、结果 | C    |                                    |

- [ ] T6

    | 任务               | 人员    | 备注                       |
    | ------------------ | ------- | -------------------------- |
    | 内容润色，格式修改 | A，B，C | 注意不同人写的部分是否连贯 |

    
