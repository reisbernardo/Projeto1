import pandas as pd
import matplotlib.pyplot as plt
from ADT import *
from tableClasses import *
import seaborn as sns
sns.set_style("whitegrid")


def create_tree(path, t_class):
    df = pd.read_excel(f"../Datasets/{path}.xlsx")
    tree = AVL_Tree()
    for row in df.values:
        tree.insert(t_class, row)
    return tree

def get_table_values(root, func):
    dic = {}
    dic = func(root, dic)
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    dic = {k: dic[k] for k in list(dic)[:10]}
    return dic

def create_results(dic):
    [print(i, "with", j, "participants") for i,j in dic.items() if j == max(dic.values())]
    plt.bar(dic.keys(), dic.values())
    plt.xticks(rotation=315)
    plt.show()


#Country with the most participants
t = create_tree("Athletes", Athletes)
c = get_table_values(t.root, t.c_w_m_participants)
print("The country(ies) with the most participants is: ")
create_results(c)

#Sport with the most participants
s = get_table_values(t.root, t.s_w_m_participants)
print("\nThe sport(s) with the most participants is: ")
create_results(s)

#Country with the most coaches

#Sport with the most coaches

#Sport with most participants

#Sport with most female participants

#Country with most gold medals

#Contry with most total of medals

#Country with most teams

#Is there more female or male teams?