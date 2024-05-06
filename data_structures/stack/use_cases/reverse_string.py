"""
---- Reverse String ----

- Description: Reverse a string using a stack.

- Example:

# String: "I am Julio Cesar"
# Reverse String: "raseC oiluJ ma I"

# String: "Shhh this is a secret"
# Reverse String: "terces a si siht hhhS"

"""

from . import Stack

def reverse_string(string):
    stack = Stack()
    reverse = ""

    for letter in string:
        stack.push(letter)

    for item in string:
        reverse += stack.pop()

    return reverse
