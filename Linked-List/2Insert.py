# Insert at begining , end and at position


class Node:

    def __init__(self , data :int) -> None:
        self.data = data 
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head : Node | None = None


    def insert_at_begining(self , data : int) -> None:

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_at_end(self ,data :int) ->  None:

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head 

        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_at_position(self , position : int , data :int)-> None:

        if position < 0:
            raise IndexError("Invalid position")

        if position == 0:
            self.insert_at_begining()
            return

        current = self.head 
        index = 0

        while current is not None and  index < position - 1:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Position out of range")

        new_node = Node(data)

        new_node.next = current.next

        current.next = new_node

    def display(self) -> None:
        # display linked list 

        if self.head is None:
            print("Linked list is empty")
            return

        current  = self.head 

        while current is not None:
            print(current.data , end = " ->")
            current = current.next

        print("None")        

ll = LinkedList()

ll.insert_at_begining(20)
ll.insert_at_begining(10)

ll.insert_at_end(40)
ll.insert_at_position(2, 30)   

ll.display()