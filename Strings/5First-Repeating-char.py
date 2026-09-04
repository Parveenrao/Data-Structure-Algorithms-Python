# find the first repeating char 


def frist_repeating_char(s : str) -> str | None:

    freq = {}

    for char in s:

        freq[char] = freq.get(char , 0) + 1


    for char in s:

        if freq[char] > 1:
            return char

    return None        