"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        # If the item is an integer, convert it to string
        if isinstance(item, int):
            item = str(item)
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    return frequencies
