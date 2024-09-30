
# Algorithm to convert infix expression to postfix expression
# 1. Create an empty stack to hold operators
# 2. Create an empty string to hold output
# 3. For each character in the infix expression:
#    a. If the character is an operand, add it to the output
#    b. If the character is '(', push it to the stack
#    c. If the character is ')', pop and output from the stack until an '(' is encountered
#    d. If the character is an operator:
#       i. Pop and output from the stack until an operator with lower precedence is encountered
#       ii. Push the current operator to the stack
# 4. Pop all the operators from the stack and add them to the output


# Function to return precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to perform infix to postfix conversion
def infix_to_postfix(expression):
    stack = []  # stack to hold operators
    output = ''  # output string

    for char in expression:
        # If the character is an operand, add it to output
        if char.isalnum():
            output += char
        # If the character is '(', push it to stack
        elif char == '(':
            stack.append(char)
        # If the character is ')', pop and output from the stack
        # until an '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        # An operator is encountered
        else:
            # Pop and output from the stack until an operator with lower precedence is encountered
            while stack and precedence(stack[-1]) >= precedence(char):
                output += stack.pop()
            stack.append(char)

    # pop all the operators from the stack
    while stack:
        output += stack.pop()

    return output

# Example usage
if __name__ == "__main__":
    expression = "a+b*(c^d-e)^(f+g*h)-i"
    print("Infix Expression: ", expression)
    print("Postfix Expression: ", infix_to_postfix(expression))