# Remove duplicate from sorted list

from typing import Optional

class ListNode:

    def __init___(self , val : int , next : Optional["ListNode"] = None):
        self.val = val 
        self.next  = next 


class Solution:

    def duplicate(self , head : Optional[ListNode]) -> Optional[ListNode]:

        values = []

        current = head 

        while current is not None:

            if not values or values[-1] != current.val:
                values.append(current.val)

            current = current.next


        dummy = ListNode(0)                         # space complexity O(n) , store every linked list element 

        tail = dummy

        for value in values:
            tail.next = ListNode(values)
            tail = tail.next

        return dummy.next
    


# optimal 

class Solution:

    def hasduplicate(self , head : Optional[ListNode]) -> Optional[ListNode]:

        current = head 

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next

            else:
                current = current.next 

        return head                



