# Merge Two sorted list 

from typing import Optional

class ListNode:

    def __ini__(self , val : int , next : Optional["ListNode"] = None):
        self.val = val 
        self.next = next


    def merge_list(self, list1 : Optional[ListNode] , list2 : Optional[ListNode]) -> Optional[ListNode]:

        values = []

        current = list1
        while current is not None:           # travers first list O(n)
            values.append(current.val)

            current = current.next 

        current  = list2                     # traverse 2nd list O(m)
        while current is not None:
            values.append(current.val)

            current = current.next 


        values.sort()                        # take O(n + m)log(n+m)

        if not values:
            return None
        
        head = ListNode(values[0])            

        tail = head 

        for value in values[1:]:
            tail.next = ListNode(value)   # create new list take O(n+m)
            tail = tail.next 

        return head    
                      # total O(n)+O(m)+O((n+m)log(n+m))+O(n+m)


# optimal 

class ListNode:

    def __ini__(self , val : int , next : Optional["ListNode"] = None):
        self.val = val 
        self.next = next


    def merge_two_list(self , list1 : Optional[ListNode] , list2 : Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        tail  = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next  = list2
                list2 = list2.next

            tail = tail.next

        # attach remaining nodes 

        if list1:
            tail.next = list1

        else:
            tail.next = list2

        return dummy.next                        

