# delete operation in singly linked list 

class Node:

    def __init__(self , data :int) -> None:
        self.data = data
        self.next : "Node| None" = None


class Linkedlist:

    def __init__(self) -> None:

        self.head : Node | None = None


    # delete at begining 
    def delete_at_begining(self) -> None:

        if self.head is None:
            raise IndexError("Linked List is empty")

        self.head = self.head.next

    # delete at end 
    def delete_at_end(self) -> None:

        if self.head is None:
            raise IndexError("Linked List is empty")

        if self.head.next is None:
            self.head = None
            return

        current = self.head 

        while current.next.next is None:
            current = current.next 

        current.next = None

    def delete_at_position(self , position : int) -> None:    

        if position < 0:
            raise IndexError("Invalid position")

        if position == 0:
            return self.delete_at_begining()


        current  = self.head 

        for _ in range(position-1):

            if current.next is None:
                raise IndexError("Position out of range")

            current = current.next 

        if current.next is  None: 
            raise IndexError('Position out of range')

        current.next = current.next.next                       