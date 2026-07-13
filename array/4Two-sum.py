# Two sum question 

class Sum:

    def two_sum(self, nums , target):

        seen = {}

        for i in range(len(nums)):

            need = target - nums[i]

            if need in seen:
                return [seen[need], i]
            
            seen[nums[i]] = i

        return []


sum = Sum()

arr1 = [2, 3, 5 ,9, 5]

print(sum.two_sum(arr1 , 14))

