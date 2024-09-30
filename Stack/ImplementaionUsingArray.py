
# Algorithm:
# 1. Create an empty stack
# 2. Implement the following methods:
#    a. create_stack: Create an empty stack
#    b. is_empty: Check if the stack is empty
#    c. push: Add an element to the top of the stack
#    d. pop: Remove and return the top element from the stack
#    e. peek: Return the top element of the stack without removing it
#    f. size: Return the number of elements in the stack

# Complexity Analysis:
# All the operations have a time complexity of O(1).
# Therefore, the overall time complexity of the stack implementation is O(1).
# Space complexity is O(n), where n is the number of elements in the stack.


class Stack:
    def __init__(self):
        self.stack = []

    def create_stack(self):
        stack = []
        return stack
    
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Output: 3
    print(s.peek())  # Output: 2
    print(s.size())  # Output: 2
    print(s.is_empty())  # Output: False