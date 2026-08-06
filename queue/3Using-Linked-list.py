# Queue using linked-list 

# queue follow FIFO , in linked list implementatio we have to main two pointers , front points to first element , rear points to last element


from typing import Any

class Node:
    def __init__(self , data : int):
        self.data : Any = data 
        self.next = Node | None = None


class Queue:
    def __init__(self) -> None:
        self.front = Node |None = None 
        self.rear = Node |None = None

        self._size : int = 0

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self , value: int) -> None:

           # insert element thorugh rear of the queue

           new_node = Node(value)

           if self.is_empty():
                self.front = self.rear = new_node

           else:
                self.rear.next = new_node
                self.rear = new_node

           self._size += 1     

    def dequeue(self) -> Any:

         # Remove and return the first element

         if self.is_empty():
              raise IndexError("Cannot delete from empty queue")

         value = self.front.data 
         self.front = self.front.next

         self._size -= 1

    def peek(self) -> Any:             # any because , queue is designed to store any type of element

         if self.is_empty():
              raise IndexError("")  

         return self.front.data


    def size(self) -> int:

         # return size of queue 

         return self._size


    def display(self) -> None:

         # print all queue elements 

         if self.is_empty():
              print("Queue is empty")
              return 

         current = self.front

         while current is not None:
              print(current.data , end = "")
              current = current.next 

         print("None") 

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return not self.is_empty()                                     