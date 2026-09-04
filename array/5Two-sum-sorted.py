# Two sum when array is sorted 


class Sum:

    def two_sum(self , arr , target):

        left = 0

        right = len(arr)-1

        while left < right:

            current_sum = arr[left] + arr[right]

            if current_sum == target:
                return [left , right] 

            elif current_sum < target:
                left += 1

            else:
                right -= 1

        return []


sum = Sum()

arr1 = [1 ,2 ,3 ,4, 5, 6]

print(sum.two_sum(arr1 , 11))