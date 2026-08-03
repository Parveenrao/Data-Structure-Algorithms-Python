""" 

=> Stack Using Linked List 



"""

from typing import Optional

class Node:

    def __init__(self , value : int) -> int: 

        self.value : int = value 
        self.next : Optional["Node"] = None


class Stack:

    # stack implementation using linked list  

    def __init__(self) -> None:
        self._top :Optional[Node] = None
        self._size : int = 0

    def push(self, value:int) -> None:

        new_node = Node(value)

        new_node.next = self._top
        self._top = new_node

        self._size += 1

    def pop(self) -> int:

        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")

        value = self._top.value

        self._top = self._top.next 

        self._size -=1

        return value

    def peek(self) -> int:

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._top.value

    def is_empty(self) -> bool:

        return self._top is None

    def size(self) -> int:

        return self._size

    def display(self) -> None:

        if self.is_empty():
            print("stack is empty")
            return

        current = self._top

        print("Top")

        while current is not None:
            print(f"|{current.value}") 

            current = current.next

        print("Bottom")

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("\nTop:", stack.peek())

print("Removed:", stack.pop())

stack.display()

print("Size:", stack.size())

print("Empty:", stack.is_empty())                           