"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    temp = items
    current_length = len(temp)
    for i in range (0, len(temp)-1):
        if (i+1 == current_length):
            frequencies[temp[i+1]] = 1
            break
        count = 1
        #if the element is an integer, convert it to string
        if isinstance(temp[i], int):
            temp[i] = str(temp[i])

        for k in range (i+1, current_length):
            #if the element is an integer, convert it to string
            if isinstance(temp[k], int):
                temp[k] = str(temp[k])
            if (temp[k] == temp[i]):
                count += 1
                del temp[k]

        frequencies[temp[i]] = count
        current_lenth = len(temp)


    return frequencies
