import pandas as pd
from ADT import *
from tableClasses import *

df = pd.read_excel("Datasets/Athletes.xlsx")
lista = df.values

t = AVL_Tree()

for row in lista:
    t.insert(Athletes, row)
t.inOrder(t.root)