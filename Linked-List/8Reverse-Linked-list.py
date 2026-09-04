# Reverse linked list 


# brute force 

from typing import Optional

class ListNode:

    def __init__(self , val : int , next : Optional[ListNode] = None):
        self.val = val 
        self.next  = next 


class Solution:

    def reverse(self , head : Optional[ListNode]) -> Optional[ListNode]:

        stack : list[int] = []

        current = head 

        while current is not None:
            stack.append(current.val)

            current = current.next

        current = head 

        while current:

            current.val = stack.pop()
            current = current.next

        return head


# Optimal 


class Solution:

    def reverse(self, head:Optional[ListNode]) -> Optional[ListNode]:

        prev : Optional[ListNode] = None
        current : Optional[ListNode] = head

        while current:
            next_node = current.next 

            current.next = prev 

            prev = current 

            current.next = next_node

        return prev    
