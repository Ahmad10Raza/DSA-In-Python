
# Algorithm to evaluate a prefix expression
# 1. Reverse the prefix expression
# 2. Iterate over the expression:
#    a. If the character is an operand, push it to the stack
#    b. If the character is an operator:
#       i. Pop two operands from the stack
#       ii. Perform the operation and push the result back to the stack
# 3. The result is the last element in the stack



def evaluate_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    # Reverse the prefix expression
    expression = expression[::-1]

    # Iterate over the expression
    for char in expression:
        if char.isdigit():
            # Push operand to stack
            stack.append(int(char))
        elif char in operators:
            # Pop two operands from stack
            operand1 = stack.pop()
            operand2 = stack.pop()

            # Perform the operation and push the result back to stack
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)

    # The result is the last element in the stack
    return stack[0]

# Example usage
expression = "*+23+45"
result = evaluate_prefix(expression)
print(f"The result of the prefix expression '{expression}' is: {result}")