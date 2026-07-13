# Implement Stack using List 


class Stack:

    def __init__(self) -> None:
        self._stack : list[int] = []


    def push(self , item) -> None:
        # insert element at the top of stack 

        self._stack.append(item)

    def pop(self) -> int:
        # remove and return the top element

        if self.is_empty():
            raise IndexError("Stack Underflow")
        
        return self._stack.pop()
    
    def peek(self) -> int:
        # return the top element
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._stack[-1]

    def is_empty(self) -> bool:
        # return true if the stack is empty
        return len(self._stack) == 0

    def size(self) -> int:
        # Display the size of element in stack 

        if self.is_empty():
            print("Stack is empty")
            return
        
        return len(self._stack)

    def __len__(self) -> int:

        return len(self._stack)

    def __repr__(self) -> str:
        return f"Stack({self._stack})" 

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)          # Stack([10, 20, 30])
print(stack.peek())   # 30
print(stack.pop())    # 30
print(stack.size())   # 2

print(repr(stack))  

