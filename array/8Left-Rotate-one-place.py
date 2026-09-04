# Left rotate by one place 


# brute force 

def left_rotate(nums):

    n = len(nums)

    temp = [0] * n

    for i in range(n-1):

        temp[i] = nums[i+1]

        temp[n-1] = nums[0]

    return temp


# in place 

def left(num):

    first = num[0]

    for i in range(len(num)-1):

        num[i] = num[i+1]

        num[-1] = first

    return num     


   

    