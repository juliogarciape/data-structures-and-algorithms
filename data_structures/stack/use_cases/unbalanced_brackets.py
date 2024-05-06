"""
---- Determine if Brackets are Unbalanced ----

- Description: Determine whether a set of brackets is balanced or not by making use of the stack data structure.

- Examples of Balanced Brackets:
# { }
# { } { }
# ( ( { [ ] } ) )

- Examples of Unbalanced Brackets:
# ( ( )
# { { { ) } ]
# [ ] [ ] ] ]

"""

from . import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_unbalanced(paren_string):
    stack = Stack()

    for i in paren_string:
        if i in "({[":
            stack.push(i)
        else:
            if stack.is_empty():
                return True
            else:
                if is_match(stack.peek(), i):
                    stack.pop()
    
    if stack.is_empty():
        return False
    else:
        return True
