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
    def __init__(self, table): #Exclude columns 0 and 6
        self.team = table[0]
        self.gold = table[1]
        self.silver = table[2]
        self.bronze = table[3]
        self.total = table[4]

class Teams:
    def __init__(self, table):
        self.name = table[0]
        self.sport = table[1]
        self.country = table[2]
        self.gender = table[3]
        