"""

=> Doubly Linked List 

    -> A ddl is a ll where each node store 

       1. Data 
       2. prev (pointer to previous node)

       3. next (pointer to next node)



"""

# implementation 

from typing import Optional

class Node:

    def __init__(self , data :int) -> None:
        self.data :int = data 
        self.next :Optional["Node"] = None
        self.prev : Optional["Node"] = None


node1 = Node(10)

node2 = Node(20)

node1.next = node2
node2.prev = node1

print(node1.data) # 10

print(node1.next.data) # 20

print(node2.prev.data) # 10

