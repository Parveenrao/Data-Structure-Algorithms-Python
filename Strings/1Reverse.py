# Reverse the given string 

# Using pythonic way 

def reverse(s : str) -> str:

    return s[::-1]


print(reverse("Parveen"))


# Brute force 


def reverse(s : str) -> str:

    reversed = ""

    for i in range(len(s)-1 , -1 , -1):
        reversed += s[i]

    return reversed


# now using stack 

def reverse(s : str) -> str:

    stack = []

    # push every character 

    for num in s:
        stack.append(num)

    reversed = ""

    while stack:

        reversed += stack.pop()

    return reversed



# Opitmal 

def reverse_string(s: str) -> str:
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    s = "hello"

    print(reverse_string(s))



