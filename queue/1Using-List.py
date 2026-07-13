# Queue implementation in python delete at front , append at end , support fifo 


class Queue:

    def __init__(self) -> None:
        self._queue : list[int] = []

    # enqueue

    def enqueue(self, data) -> None:
        self._queue.append(data)
        print(f"{data} inserted into queue")

    # dequeue

    def dequeue(self) -> None:

        if self.is_empty():
            print("Queue is empty")  

        removed = self._queue.pop(0)

        print(f"{removed} removed from queue") 

    # front element 
    def front_element(self) -> int:

        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Front element" , self._queue[0])

    # Rear element 

    def rear_element(self) -> int:

        if self.is_empty():
            print("Queue is empty") 
            return

        print("Rear Element" , self._queue[-1])

    # check is queue is empty 
    def is_empty(self) -> bool:

        return len(self._queue) == 0

    # diplay queue 
    def display(self) -> list[int]:
        if self.is_empty():
            print("Queue is empty")

            return

        print("Queue" , self._queue)

    # size of queue
    def size(self) -> int:
        return len(self._queue) 


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()

q.front_element()
q.rear_element()

print("Size:", q.size())              

