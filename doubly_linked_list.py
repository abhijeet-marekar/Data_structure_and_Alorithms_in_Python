class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.next_node = None
        self.pre_node = None
        
class doubly_linkedList:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.Number_of_Nodes = 0
        
    def insert_front(self,data):
        
        new_node = Node(data)
        self.Number_of_Nodes += 1
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head 
            self.head.pre_node = new_node 
            self.head = new_node 
            
    def insert_end(self,data):
        new_node = Node(data)
        self.Number_of_Nodes += 1
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre_node = self.tail 
            self.tail.next_node = new_node 
            self.tail = new_node 
    
    def traverse_forward(self):
        
        current_node = self.head 
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node 
        
    def traverse_backward(self):
        
        current_node = self.tail 
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.pre_node   
            
    def size(self):
        
        return print('Size of list : ', self.Number_of_Nodes)
    
    
    def remove(self, data):
        
        current_node = self.head 
        last_node = None
        
        if current_node is None:
            return print('List is empty !!!')
        
        while current_node is not None and current_node.data != data:
            last_node = current_node 
            current_node = current_node.next_node 
        
        if current_node is None:
            return print("Search Miss!!! Item is not in the List.")
        else:
            last_node.next_node = current_node.next_node
            current_node.pre_node = last_node
        self.Number_of_Nodes -= 1

if __name__ == '__main__':

    dl = doubly_linkedList()
    dl.insert_end(1)
    dl.insert_end(10)
    dl.insert_end(100)
    dl.insert_end(1000)
    dl.insert_end(10001)
    dl.insert_end(10000)
    dl.insert_end(100000)  

    dl.traverse_forward()

    dl.remove(1000) 
    
    dl.traverse_forward()     