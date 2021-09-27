# Each class represents one dataset (table) and its attributes 
# from the 2021 Olympics dataset from Kaggle
# source: https://www.kaggle.com/arjunprasadsarkhel/2021-olympics-in-tokyo

class Athletes:
    def __init__(self, table):
        self.name = table[0]
        self.country = table[1]
        self.sport = table[2]
        
class Coaches:
    def __init__(self, table):
        self.name = table[0]
        self.country = table[1]
        self.sport = table[2]

class EntriesGender:
    def __init__(self, table):
        self.sport = table[0]
        self.female = table[1]
        self.male = table[2]
        self.total = table[3]
        
class Medals:
    def __init__(self, table):
        self.rank = table[0]
        self.team = table[1]
        self.gold = table[2]
        self.silver = table[3]
        self.bronze = table[4]
        self.total = table[5]
        self.total_rank = table[6]

class Teams:
    def __init__(self, table):
        self.name = table[0]
        self.sport = table[1]
        self.country = table[2]
        self.gender = table[3]
        