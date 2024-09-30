
# Algorithms for postfix expression evaluation:
# 1. Create an empty stack to hold operands
# 2. For each token in the postfix expression:
#    a. If the token is an operand, push it to the stack
#    b. If the token is an operator:
#       i. Pop the top two elements from the stack
#       ii. Apply the operator to the two elements
#       iii. Push the result back to the stack
# 3. The final result is the only element left in the stack


class PostfixEvaluator:
    def __init__(self):
        self.stack = []

    def evaluate(self, expression):
        for token in expression.split():
            if token.isdigit():
                self.stack.append(int(token))
            else:
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self._apply_operator(token, operand1, operand2)
                self.stack.append(result)
        return self.stack.pop()

    def _apply_operator(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '^':
            return operand1 ** operand2
        else:
            raise ValueError(f"Unknown operator: {operator}")

if __name__ == "__main__":
    expression = "3 4 + 2 * 7 /"
    evaluator = PostfixEvaluator()
    result = evaluator.evaluate(expression)
    print(f"Result of '{expression}' is {result}")