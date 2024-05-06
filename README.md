# Data Structures and Algorithms (Python)

## Data Structures

#### Stack:

```python
# ---- Basic Example ----

my_stack = Stack() # Initialize a stack
print(my_stack.is_empty())
my_stack.push("Book A") # Add to stack
my_stack.push("Book B")
print(my_stack.get_stack()) # Get the stack
my_stack.push("Book C")
print(my_stack.get_stack())
my_stack.pop() # Remove last addition from stack
print(my_stack.get_stack())
print(my_stack.is_empty()) # Get if stack is empty
print(my_stack.peek()) # Get last addition from stack
```

### Use cases for stack:

- Determine if the brackets are unbalanced
- Reverse String
- Convert Integer to Binary
