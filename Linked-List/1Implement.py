""" 

=> Linked List 

    -> A LL is a linear data structure where each element store 

        1. Data 
        2. Reference (pointer) to the next node 

        
    -> unlike list , elements are not stored contiguously in memory    

"""

class Node:

    def __init__(self , data : int) -> None:
        self.data = data 
        self.next = None

node1 = Node(10)

node2 = Node(20)

node1.next = node2

print(node1.data)

print(node1.next.data)

print(node2.data)

print(node2.next)