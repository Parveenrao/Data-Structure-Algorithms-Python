# Search element in linked list 


def search(self , target : int) -> bool:

    current = head 

    while current is None:

        if current.data == target:
            return True
        
        current = current.next 

    return False    