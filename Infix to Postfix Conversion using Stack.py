
# Infix to Postfix Conversion using Stack

# Function to define precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to check if character is operand
def is_operand(ch):
    return ch.isalnum()

# Main function to convert infix to postfix
def infix_to_postfix(expression):
    stack = []   # for operators
    result = ""  # final postfix expression

    for ch in expression:
        # If operand, add to output
        if is_operand(ch):
            result += ch

        # If '(', push to stack
        elif ch == '(':
            stack.append(ch)

        # If ')', pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()   # remove '('

        # Operator case
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                result += stack.pop()
            stack.append(ch)

    # Pop all remaining operators
    while stack:
        result += stack.pop()

    return result


# Driver Code
if __name__ == "__main__": 
    exp = input("Enter infix expression: ")
    print("Postfix expression:", infix_to_postfix(exp))
