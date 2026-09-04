# Given a string , find the first character that appears only once.


# brute force 


def first_non_repeating_character(s : str) -> str | None:

    for i in range(len(s)):

        count = 0

        for j in range(len(s)):

            if s[i] == s[j]:
                count += 1

        if count == 1:
            return s[i]

    return None



# optimal 


def first_non_repeating(s : str) -> str | None:

    freq = {}

    for char in s:

        freq[char] = freq.get(char , 0) + 1


    for char in s:

        if freq[char] == 1:
            return char 

    return None       