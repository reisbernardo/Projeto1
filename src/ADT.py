# Node class that stores each table class and its attributes 
class Node:
    def __init__(self, table_class, table):
        self.obj = table_class(table)
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
    
    
class AVL_Tree:
    #ADT Methods
    def __init__(self):
        self.root = None
        
    def __insert(self, n, table_class, table, attr):
        attribute = getattr(n.obj, attr)
        if table[0] < attribute:
            if(n.left == None):
                n.left = Node(table_class, table)
                n.left.parent = n
                self.__inspect_insertion(n.left)
            else:
                self.__insert(n.left, table_class, table, attr)
        elif table[0] > attribute:
            if(n.right == None):
                n.right = Node(table_class, table)
                n.right.parent = n
                self.__inspect_insertion(n.right)
            else:
                self.__insert(n.right, table_class, table, attr)

        
    def insert(self, table_class, table, attr):
        if self.root == None:
            self.root = Node(table_class, table)
        else:
            self.__insert(self.root, table_class, table, attr)
    
    
    def __inspect_insertion(self, n, path=[]):
        if n.parent == None: 
            return
        path = [n] + path

        left_height = self.getHeight(n.parent.left)
        right_height = self.getHeight(n.parent.right)

        if abs(left_height-right_height) > 1:
            path = [n.parent] + path
            self.__rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + n.height 
        if new_height > n.parent.height:
            n.parent.height = new_height

        self.__inspect_insertion(n.parent,path)
       
        
    def __rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self.__rightRotate(z)
        elif y == z.left and x == y.right:
            self.__leftRotate(y)
            self.__rightRotate(z)
        elif y == z.right and x == y.right:
            self.__leftRotate(z)
        elif y == z.right and x == y.left:
            self.__rightRotate(y)
            self.__leftRotate(z)

        
    def __rightRotate(self, z):
        aux_parent = z.parent 
        y = z.left
        aux = y.right
        
        y.right = z
        z.parent = y
        z.left = aux
        
        if aux != None: 
            aux.parent = z
            
        y.parent = aux_parent
        
        if y.parent == None:
                self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y		
        z.height = 1 + max(self.getHeight(z.left),
                            self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                            self.getHeight(y.right))
        
        
    def __leftRotate(self, z):
        aux_parent = z.parent 
        y = z.right
        aux = y.left

        y.left = z
        z.parent = y
        z.right = aux

        if aux != None: 
            aux.parent = z
            
        y.parent = aux_parent

        if y.parent == None: 
            self.root=y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.getHeight(z.left),
                            self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                            self.getHeight(y.right))
        
        
    def getHeight(self, n):
        if n == None:
            return 0
 
        return n.height


    def inOrder(self, n):
        if n != None:
            self.inOrder(n.left)
            print(n.obj.name, end=" ")
            self.inOrder(n.right)
            
    # Data analysis method, it stores the data acording to attribute value passed into the function
    # If its a number then it will add all occurrences
    # If its an atribute then it will just create one instance in the dictionary
    # returns a dictionary to be used in ploting the charts
    def data_analysis(self, n, dic, attr1, attr2):
        if n != None:
            attribute1 = getattr(n.obj, attr1)
            if type(attr2) is not int:
                attribute2 = getattr(n.obj, attr2)
            else:
                attribute2 = attr2
                
            if attribute1 not in dic:
                dic[attribute1] = attribute2
            else:
                dic[attribute1] += attribute2
            self.data_analysis(n.left, dic, attr1, attr2)
            self.data_analysis(n.right, dic, attr1, attr2)
        return dic