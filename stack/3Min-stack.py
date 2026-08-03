""" 

=> Min-Stack 

    -> Min stack is a special type of stack that support all stack operation  and can return 
       the minimum element in O(1) time

    -> Operation 

     1. Push(x) -> Push an element onto the stack 
     2. pop()   -> remove the top element 
     3. Top()   -> Return the top element 
     4. getmin() -> Return the current minimum element in the stack   


"""

from typing import List

class MinStack:

    def __init__(self) -> None:
        self._stack : List[int]     = []
        self._min_stack : List[int] = []


    def push(self , value : int) -> None:

        if not isinstance(value , int):
            raise IndexError("Only integer values are allowed")
        
        self._stack.append(value)

        if not self._min_stack or value <= self._min_stack[-1]:    
            self._min_stack.append(value)

    def pop(self) -> int:

        if self.is_empty():
            raise IndexError("Cannot import from an empty stack") 

        value = self._stack.pop()

        if value == self._min_stack[-1]:
            self._min_stack.pop()

        return value


    def top(self) -> int:

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._stack[-1]


    def get_min(self) -> int:

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._min_stack[-1]

    def is_empty(self) -> bool:

        return len(self._stack) == 0


    def size(self)  -> int:

        return len(self._stack)


    def __len__(self) -> int:

        return len(self._stack)

    def __len__(self) -> int:
        # Support len(stack).
        return len(self._stack)

    def __repr__(self) -> str:
        # Developer-friendly representation
       
        return (
            f"MinStack("
            f"stack={self._stack}, "
            f"min={self._min_stack[-1] if self._min_stack else None})"
        )            
    


if __name__ == "__main__":
    stack = MinStack()

    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.push(2)

    print(stack)
    # MinStack(stack=[5, 3, 7, 2], min=2)

    print("Top:", stack.top())          # 2
    print("Minimum:", stack.get_min())  # 2

    stack.pop()

    print("Top:", stack.top())          # 7
    print("Minimum:", stack.get_min())  # 3

    print("Size:", stack.size())        # 3    