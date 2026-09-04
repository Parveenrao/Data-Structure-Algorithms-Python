from collections import deque


class Reverse:

    def reverse_queue(self, q):

        stack = []

        while q:
            stack.append(q.popleft())

        while stack:
            q.append(stack.pop())

        return q


def main():

   
    q = deque([1, 2, 3, 4, 5])

    print("Original Queue:", q)

    
    obj = Reverse()

    
    obj.reverse_queue(q)

    print("Reversed Queue:", q)


if __name__ == "__main__":
    main()