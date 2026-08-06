""" 

=> Implement Monotonic Stack 

    -> Keep element in increasing order from bottom to top


"""


class MonotonicStack:

    def __init__(self) -> None:
        self._stack : list[int] = []


    def push(self, val: int) -> None:    

        # Push a value while maintaining order of stack 
        while self._stack and self._stack[-1] > val:
            self._stack.pop()


        self._stack.append(val)

    def pop(self) -> int:

        "Remove and return the top element"
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._stack.pop()

    def peek(self) -> int:
        "Return the top element"

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._stack[-1]

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def size(self) -> int:  
        return len(self._stack)

    def __len__(self) -> int: 
        return len(self._stack)

    def clear(self) -> None:
        return self._stack.clear()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._stack})"

stack = MonotonicStack()

for num in [5, 3, 8, 2, 6]:
    stack.push(num)

print(stack)          # MonotonicIncreasingStack([2, 6])
print(stack.peek())   # 6
print(stack.pop())    # 6
      