""" 

=> Search Element In Doubly Linked list



"""
                                            
class DoublyLinkedList:
                             
    def __init__(self):                                # best case first node is target O(1)
        self.head = None                               # wrost case , traverse linked list O(n)

    def search(self , target:int ) -> bool:

        current = self.head 

        while current:

            if current.data == target:
                return True

            current = current.next 

        return False        


# Interviewer ask return its index 

def search_element(self , target : int) -> int:

    current = self.head

    index = 0

    while current:

        if current.data == target:
            return index

        current = current.next 

    return -1     

    