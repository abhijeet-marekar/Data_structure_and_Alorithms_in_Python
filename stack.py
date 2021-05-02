''' Stack is an abstract data type. It can be implemented either with arrays 
or linked list. Here stack is implemeted using array becuase of ease of 
implementation and pop, push and peak operatation gives O(1) running time. 

NOTE: stack follows LIFO (last In First Out) Structure
author : Abhijeet Marekar
'''

class stack:
    
    def __init__(self):
        
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        data = stack[-1]
        
        del self.stack[-1]
        
        return data 
    
    def peak(self):
        return self.stack[-1]
    
    def is_empty(self):
        
        return self.stack == []
    
    def size(self):
        
        return len(self.stack)