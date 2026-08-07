# Find the 2nd largest element in the array , is no element return -1


class Second:
    
    def element(self ,arr)-> int:

        arr.sort()

        return arr[-2]
    
second = Second() 

print(second.element([1, 2, 3, 4, 5]))


#----------------------------------------------------------------------------

# optimal 

class Optimal:

    def element(self ,arr):

        if not arr:
            raise ValueError("Array is empty")

        if len(arr) < 2:
            return -1


        first  = float("-inf")
        second = float("-inf")

        for num in arr:

            if num > first:
                second = first
                first = num 

            elif first > num > second:
                second = num 

        return -1 if second == float("-inf") else second    

optimal = Optimal()

print(optimal.element([2, 2, 2, 2]))

print(optimal.element([2]))


print(optimal.element([2, 5 , 9 , 11, 23, 24, 3]))