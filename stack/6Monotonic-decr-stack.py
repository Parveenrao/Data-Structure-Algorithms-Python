""" 

=> Monotonic Decreasing Stack keep elements in decreasing order from bottom to top


"""

class MonotonicDecreasingStack:
    """
    A stack that maintains elements in decreasing order
    (from bottom to top).

    Example:
        Bottom
        10
         8
         5
         2
        Top
    """

    def __init__(self) -> None:
        self._stack: list[int] = []

    def push(self, value: int) -> None:
        """
        Push a value while maintaining decreasing order.

        Any element smaller than the new value is removed.
        """
        while self._stack and self._stack[-1] < value:
            self._stack.pop()

        self._stack.append(value)

    def pop(self) -> int:
        """
        Remove and return the top element.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._stack.pop()

    def peek(self) -> int:
        """
        Return the top element without removing it.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._stack[-1]

    def is_empty(self) -> bool:
        """
        Check whether the stack is empty.
        """
        return len(self._stack) == 0

    def size(self) -> int:
        """
        Return the number of elements in the stack.
        """
        return len(self._stack)

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        """
        self._stack.clear()

    def display(self) -> None:
        """
        Print the stack from bottom to top.
        """
        print(self._stack)