# detect cycle in linked list 


from typing import Optional

class ListNode:

    def __init__(self , val : int , next : Optional["ListNode"] = None):
        self.val = val 
        self.next = next

class Solution:

    def hascycle(self,head : Optional[ListNode]) -> bool:

        visited : set[ListNode] = set()   # Sc  O(n) we store every node in set

        current = head 

        while current is not None:       # Tc O(n) , traverse all the list
            if current in visited:
                return True
            visited.add(current)

        return False           
    

# optimal 

class ListNode:

    def __init__(self ,val : int , next : Optional["ListNode"] = None):
        self.val = val 

        self.next = next 

class Solution:

    def cycle(self , head : Optional[ListNode]) -> bool:

        current = head 

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next


            if slow == fast:
                return True
            
        return False   