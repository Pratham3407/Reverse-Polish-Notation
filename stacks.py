def infix_to_postfix(expression):
    # Define operator precedence
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3, '$':3}

    def shunting_yard(infix):
        output = []
        operators = []

        for char in infix:
            if char.isalnum():
                output.append(char)
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()
            else:
                while (operators and precedence.get(operators[-1], 0) >= precedence.get(char, 0)):
                    output.append(operators.pop())
                operators.append(char)

        while operators:
            output.append(operators.pop())

        return ''.join(output)

    return shunting_yard(expression)

def infix_to_prefix(expression):
    def reverse_string(s):
        return s[::-1]

    def swap_parentheses(s):
        return s.replace('(', 'tmp').replace(')', '(').replace('tmp', ')')

    reversed_expression = reverse_string(expression)
    swapped_expression = swap_parentheses(reversed_expression)

    postfix_expression = infix_to_postfix(swapped_expression)
    prefix_expression = reverse_string(postfix_expression)

    return prefix_expression

# Get user input
infix_expression = input("Enter an infix expression: ")

# Convert to postfix
postfix = infix_to_postfix(infix_expression)
print(f"Postfix notation: {postfix}")

# Convert to prefix
prefix = infix_to_prefix(infix_expression)
print(f"Prefix notation: {prefix}")
