
# Algorithm:
# 1. Create two queues q1 and q2
# 2. For push operation:
#    a. Add the element to q2
#    b. Move all elements from q1 to q2
#    c. Swap q1 and q2
# 3. For pop operation:
#    a. If q1 is empty, return None
#    b. Otherwise, return the front element of q1
# 4. For top operation:
#    a. If q1 is empty, return None
#    b. Otherwise, return the front element of q1
# 5. For empty operation:
#    a. Return whether q1 is empty

# Complexity Analysis:
# All operations have a time complexity of O(n) where n is the number of elements in the stack.
# The space complexity is O(n) where n is the number of elements in the stack.

# Pop operation is costly  in this implementation as we have to move all elements from q1 to q2 for every push operation.
# If we want to make pop operation costly, we can move all elements from q1 to q2 for every pop operation.
# This way, the pop operation will have a time complexity of O(n) and the push operation will have a time complexity of O(1).



from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()

    def top(self):
        if self.q1.empty():
            return None
        return self.q1.queue[0]

    def empty(self):
        return self.q1.empty()

# Example usage:
if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())  # Output: 3
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2
    print(stack.empty())  # Output: False
    print(stack.pop())  # Output: 1
    print(stack.empty())  # Output: True