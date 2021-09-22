import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ADT import *
from tableClasses import *
sns.set_style("whitegrid")


ath = pd.read_excel("Datasets/Athletes.xlsx")
t = AVL_Tree()


for row in ath.values:
    t.insert(Athletes, row)


c = t.c_w_m_participants(t.root)
c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))


c = {k: c[k] for k in list(c)[:10]}


c


c_values = c.values()
c_keys = c.keys()



max_value = max(c_values)
print("The country(ies) with the most participants is: ")
[print(i, "with", j, "participants") for i,j in c.items() if j == max_value]


plt.bar(c_keys, c_values)
plt.xticks(rotation=315)




