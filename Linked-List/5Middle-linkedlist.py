# find the middle of the linked list

# Brute force 

from typing import Optional

class ListNode:

    def __init__(self, val:int , next : Optional["ListNode"] = None):
        self.val = val 
        self.next = next


class Solution:

    def middle(self , head : Optional[ListNode]) -> Optional[ListNode]:

        count = 0 

        current  = head 

        while current is not None:             # Tc -> O(n)
            count += 1

            current = current.next 


        middle = count // 2

        current = head 

        for _ in range(middle):                  # O(n/2) , traverse till middle
            current = current.next 

        return current              
    

# Optimal , slow and fast pointer , fast move 2 step and slow move one , 


class ListNode:

    def __init__(self , val : int , next : Optional["ListNode"] = None):
        self.val = val 
        self.next = next 


class Solution:

    def middle(self ,head : Optional[ListNode]) -> Optional[ListNode]:

        slow = head 
        fast = head 

        while fast is not None and fast.next is not None:

            slow = slow.next 
            fast = fast.next.next

        return slow   