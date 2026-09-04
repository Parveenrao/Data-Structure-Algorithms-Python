# check whether string is palingdrome or not , read same from front and back 



# python way 

def palingdrom(s : str) -> bool:

    return s == s[::-1]


# brute force 

def palingdrome(s : str) -> bool:

    reversed = ""

    for i in range(len(s)-1 , -1 , -1):

        reversed += s[i]

    return s == reversed



# palingdrome using stack 

def palingdrome(s : str) -> bool:

    stack = []

    for char in s:
        stack.append(char)


    for char in s:

        if char != stack.pop():

            return False

    return True


# optimal


def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    s = "madam"

    print(is_palindrome(s))

