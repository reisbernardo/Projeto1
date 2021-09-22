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

def get_table_values(root, func, attr):
    dic = func(root, {}, attr)
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    dic = {k: dic[k] for k in list(dic)[:10]}
    return dic

def create_results(dic):
    [print(i, "with", j, "participants") for i,j in dic.items() if j == max(dic.values())]
    plt.bar(dic.keys(), dic.values())
    plt.xticks(rotation=315)
    plt.show()


#Country with the most participants
t1 = create_tree("Athletes", Athletes)
countries = get_table_values(t1.root, t1.data_analysis, "country")
print("The country(ies) with the most participants is: ")
create_results(countries)

#Sport with the most participants
t2 = create_tree("Athletes", Athletes)
sports = get_table_values(t2.root, t2.data_analysis, "sport")
print("\nThe sport(s) with the most participants is: ")
create_results(sports)

#Country with the most coaches
t3 = create_tree("Coaches", Coaches)
coaches = get_table_values(t3.root, t3.data_analysis, "country")
print("\nThe country(ies) with the most coaches is: ")
create_results(coaches)

#Sport with the most coaches

#Sport with most participants

#Sport with most female participants

#Country with most gold medals

#Contry with most total of medals

#Country with most teams

#Is there more female or male teams?