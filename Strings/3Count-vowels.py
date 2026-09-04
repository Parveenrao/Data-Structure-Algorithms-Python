# Count vowels in string 

# burte force 


def count(s : str) -> int:

    for char in s:

        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1

    return count


# optimal ,

def count(s : str) -> int:

    vowels = {"a" , "e" , "i" , "o" , "u"}

    count = 0
    for char in s:

        if char in vowels:
            count += 1

    return count        