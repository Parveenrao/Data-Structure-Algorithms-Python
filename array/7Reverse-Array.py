# Given an array , reverse it


# first approach , create new array 

def reverse_array(nums)-> list[int]:

    result = []

    for i in range(len(nums)-1, -1, -1):

        result.append(nums[i])

    return result


print(reverse_array([1, 2, 3,4, 5]))


# pythonic way 

def reverse_array_python(nums):

    return nums[::-1]                            # create new aaray


# using optimal in place change

class Reverse:

    def array(self , arr):

        left = 0

        right = len(arr)-1

        while left < right:

            arr[left] , arr[right] = arr[right] , arr[left]

            left += 1
            right -= 1

        return arr    
                                  