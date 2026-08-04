# Maximum Element In A Array


# Brute force , sort array and return last element 

class Element:
    
    def largest(self, arr):

        if not arr:
            raise ValueError("Array is empty")
        
        arr.sort()

        return arr[-1]
    
element = Element()


arr = [1, 4 ,5 ,2, 9 ,11]

print(element.largest(arr))


#-----------------------------------------------------------------

# optimal solution 

class Optimal:

    def largest(self , arr):

        if not arr:
            raise ValueError("Array is empty")
        
        largest = arr[0]

        for num in arr:
            if num > largest:

                largest = num 

        return largest


optimal = Optimal()

arr1 = [2]

arr2 = [1, 2, 3, 5, 3, 11]

arr3 = [-9 , -2, -3, -1]

arr4 = []

print(optimal.largest(arr1))
print(optimal.largest(arr2))
print(optimal.largest(arr3))
print(optimal.largest(arr4))


             