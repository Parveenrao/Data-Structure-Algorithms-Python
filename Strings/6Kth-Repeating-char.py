# find the kth repeating char 


def k_repeating_char(s : str , k) -> str | None:

    freq = {}

    for char in s:
        freq[char] = freq.get(char , 0) + 1


    count = 0
    for char in s:

        if freq[char] > 1:

            count += 1


            if count == k:
                return char

    return None        

            
