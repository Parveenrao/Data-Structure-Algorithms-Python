# Find the third largest element in the array , return -1 if no element found 

# Brute force 

class Third:

    def element(self , arr):
        if not arr:
            raise ValueError("Array is empty")
        
        arr.sort()
        return arr[-3]
    

# Optimal solution 

class Optimal:

    def element(self , arr):

        if not arr:
            raise ValueError("Array is empty")

        if len(arr) < 3:
            return -1

        first = second = third = float("-inf")
        for num in arr:

            if num > first:   

                third = second 
                second = first 

                first = num 

            elif first > num > second:

                third = second
                second = num 

            elif second > num > third:
                third = num 

        return -1 if third == float("-inf") else third


optimal = Optimal()



print(optimal.element([2 ,3]))

print(optimal.element([5, 9, 7]))

print(optimal.element([-1, -2, -3 , -9 ,-10]))

print(optimal.element([]))

