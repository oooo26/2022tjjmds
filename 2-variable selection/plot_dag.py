
# %%
from graphviz import Digraph
import numpy as np
import pandas as pd

Adj = pd.read_csv("dag.csv")
# nodes = Adj.columns
nodes = ["第二产业产值（万元）",
         "人均生产总值（按常住人口计算）（元）",
         "小学在校学生数（人）",
         "小学教职工人数（人）",
         "进口总值（万美元）",
         "国内旅游（万人次）",
         "增值税（元）",
         "一般公共服务支出（元）",
         "流动电话用户数目（万户）",
         "score"]
Adj = Adj.to_numpy()
p = len(nodes)

# %% graphviz
dot = Digraph(
    name="dag",
    comment="dag",
    format='pdf'
)

for index, name in enumerate(nodes):
    dot.node(str(index), name)

for i in range(p):
    for j in range(p):
        if Adj[i, j] != 0:
            dot.edge(str(i), str(j))

dot

# %% save
dot.render(directory=f"./")
# print(dot.source)
