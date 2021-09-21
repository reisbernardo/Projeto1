import pandas as pd
import matplotlib.pyplot as plt
from ADT import *
from tableClasses import *

ath = pd.read_excel("Datasets/Athletes.xlsx")

t = AVL_Tree()

for row in ath.values:
    t.insert(Athletes, row)

#Country with the most participants
c = t.c_w_m_participants(t.root)
c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
c = {k: c[k] for k in list(c)[:10]}
c_values = c.values()
c_keys = c.keys()
print(c_values)
max_value = max(c_values)
print("The country(ies) with the most participants is: ")
[print(i, "with", j, "participants") for i,j in c.items() if j == max_value]

plt.bar(c_keys, c_values)
plt.xticks(rotation=315)
plt.show()

# c_values = c.values()
# c_keys = c.keys()
# max_value = max(c_values)
# print(max_value)
# print("The country(ies) with the most participants is: ")
# [print(i) for i,j in c.items() if j == max_value]
# plt.bar(c_values, c_keys)
# plt.show()


#Sport with the most participants


#Country with the most coaches

#Sport with the most coaches

#Sport with most participants
# 
#Sport with most female participants

#Country with most gold medals

#Contry with most total of medals

#Country with most teams

#Is there more female or male teams?