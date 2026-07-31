# Queue using stack 

# take two stack , stack1 for enqueue , stack2 for dequeu


class Queue:

    def __init__(self) -> None:
        self.stack1 : list[int] = []
        self.stack2 : list[int] = []


     # enquee , thorugh rear end , last 
    def enqueue(self , item : int) -> None:
        # insert element into queue
        self.stack1.append(item)

    # dequeue remove and return the element 

    def dequeue(self) -> int:

        # Remove and return the front element 
        if self.is_empty():
            raise IndexError("Queue is empty")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop) 

        return self.stack2.pop()


    def front(self) -> int:

        # return the first element

        if self.is_empty():
            raise IndexError("Queue is empty")


        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]


    def is_empty(self) -> bool:
        # check whether queue is empty 

        return len(self.stack1) == 0 and len(self.stack2) == 0

    def display(self) -> None:
        """Display the queue from front to rear."""
        queue = self.stack2[::-1] + self.stack1
        print(queue)                     