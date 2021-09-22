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
    dic = func(root, {})
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    dic = {k: dic[k] for k in list(dic)[:10]}
    return dic

def create_results(dic):
    [print(i, "with", j, "participants") for i,j in dic.items() if j == max(dic.values())]
    plt.bar(dic.keys(), dic.values())
    plt.xticks(rotation=315)
    plt.show()


t1 = create_tree("Athletes", Athletes)
countries = get_table_values(t1.root, t1.c_w_m_participants)
print("The country(ies) with the most participants is: ")
create_results(countries)


t2 = create_tree("Athletes", Athletes)
sports = get_table_values(t2.root, t2.s_w_m_participants)
print("The sport(s) with the most participants is: ")
create_results(sports)


t3 = create_tree("Coaches", Coaches)
coaches = get_table_values(t3.root, t3.c_w_m_coaches)
print("The country(ies) with the most coaches is: ")
create_results(coaches)



