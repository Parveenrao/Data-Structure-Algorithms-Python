# Insert operation in DLL

from typing import Optional

class Node:

    def __init__(self , data : int) -> None:
        self.data = data 
        self.next :Optional["Node"] = None
        self.prev : Optional["Node"] = None


class DoublyLL:

    def __init__(self) -> None:
        self.head : Optional[Node] = None

    # insert at begining 

    def insert_at_begining(self , data : int) -> None:

        new_node = Node(data)

        if self.head is None:
            self.head = new_node  
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node           