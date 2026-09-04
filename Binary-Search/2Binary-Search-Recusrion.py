# Recursive version of binary search 

class Solution:

    def search(self , nums , target):

        def binarysearch(left , right):

            # base case 

            if left > right:
                return -1

            mid = (left + right) // 2

            # target found

            if nums[mid] == target:
                return mid

            # search right half 

            elif nums[mid] < target:
                return binarysearch(mid + 1 , right)

            else:
                return binarysearch(left , mid-1)

        return binarysearch( 0 , len(nums)-1)    

            