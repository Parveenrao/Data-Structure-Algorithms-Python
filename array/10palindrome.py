""" 

=> Given a list check wether it is plaindrome or not 
=> A palindrome reads same forward and backward 



"""


class Plaindrome:

    def check_array(self , nums : list[int]) -> bool:

        left = 0 
        right = len(nums)-1

        while left < right:

            if nums[left] != nums[right]:
                return False

            left += 1
            right -= 1

        return True


palindrome = Plaindrome()

nums = [1]

print(palindrome.check_array(nums))
         