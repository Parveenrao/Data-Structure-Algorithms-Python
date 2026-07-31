# Implement stack using queue


# when we push new element , insert it into the queue , rotate all the previous element behind it


from collections import deque

class Stack:

    def __init__(self):
        self.queue : deque[int] = deque()

    def push(self ,x) -> None:
        # push element into the stacl
        self.queue.append(x)


        for _ in range(len(self.queue) -1):

            self.queue.append(self.queue.popleft)

    # pop 

    def pop(self) -> int:

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.queue.popleft()

    # peek , top element 
    def peek(self) -> int:

        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.queue[0]

    def empty(self) -> bool:
        "check whether stack is empty"

        return len(self.queue) == 0

    def size(self) -> int:

        "size of stack"

        return len(self.queue)

    def display(self) -> None:
        # display the stack

        print(list(self.queue))

    def __len__(self) -> int:
        return len(self.queue)

    def __repr__(self) -> str:
        return f"Stack({list(self.queue)})"            
          