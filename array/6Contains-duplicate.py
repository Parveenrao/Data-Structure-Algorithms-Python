# Given an value , return true is a value appera twice 

# brute force

class Duplicate:

    def contain_duplicate(self, arr) -> bool:

        n = len(arr)

        for i in range(n):
            for j in range(i + 1 , n):

                if arr[i] == arr[j]:
                    return True
                
        return False



# Optimal 

class Optimal:

    def duplicate(self, arr) -> bool:

        seen = set()

        for nums in range(len(arr)):

            if nums in seen:
                return False
            
            seen.add(nums)

        return True    

