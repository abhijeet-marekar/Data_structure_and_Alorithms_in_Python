

class Node:
    
    def __init__(self,data): 
        self.data = data
        self.nextNode = None
    
class LinkedList:
    
    def __init__(self):
        
        self.head = None
        self.number_of_Nodes = 0
        
    def insert_start(self, data):
        
        new_node = Node(data)
        self.number_of_Nodes += 1
        
        if self.head == None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
            
    def insert_end(self, data):
        
        new_node = Node(data)
        self.number_of_Nodes += 1
        
        
        current_node = self.head
        while (current_node.nextNode is not None):
            current_node = current_node.nextNode
            
        current_node.nextNode = new_node
        
    def size(self):
        return print("Size of list : ",self.number_of_Nodes)
    
    def traverse(self):
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.nextNode
            
    def remove(self,data):
        
        
        if self.head == None:
            return print("The List is empty")
        
        current_node = self.head 
        last_node = None
        
        while current_node is not None and current_node.data != data :
            last_node = current_node
            current_node = current_node.nextNode
        
        if current_node is None:
            return print('Search Miss!! Given data is not presnt in the list.')
        
            
        if last_node is None:
            self.head = current_node.nextNode
        else:
            last_node.nextNode = current_node.nextNode            
        self.number_of_Nodes -=  1
            
            

   
ll = LinkedList()

ll.insert_start(1)
ll.insert_start(10)
ll.insert_start(100)
ll.insert_start(1000)
ll.insert_start(1000)
ll.insert_start(10000)
ll.insert_start(100000)
ll.insert_start(1000000)
ll.insert_end(-99)


ll.traverse()

ll.size()

ll.remove(100)

ll.traverse()
ll.size()
            