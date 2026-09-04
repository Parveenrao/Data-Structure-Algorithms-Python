# Right rotate array by one place 

# brute force


def right_rotate(nums):

    n = len(nums)

    temp = [0] * n

    temp[0] = nums[-1]

    for i in range(n-1):

        temp[i+1] = nums[i]

    return temp    



# in place 


def optimal(arr):

    last = arr[-1]

    for i in range(len(arr)-1, 0 , -1):
        arr[i] = arr[i-1]

    arr[0] = last

    return arr    