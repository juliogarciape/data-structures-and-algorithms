"""
---- Convert Integer to Binary ----

- Description: Convert integer values to their binary equivalent.

- Example:

# Integer: 95
# Binary: 1011111

# Integer: 84
# Binary: 1010100

"""

from . import Stack

def convert_int_to_bin(number):
    stack = Stack()
    result = number
    binary = ""

    while result != 0:
        result = result / 2
        
        if result.is_integer():
            stack.push(0)
        else:
            stack.push(1)
        
        result = int(result)

    while not stack.is_empty():
        binary += str(stack.pop())

    return binary
