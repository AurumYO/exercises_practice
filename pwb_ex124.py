# Exercise 124: Evaluate Postfix (solved 58 Lines)
# Evaluating a postfix expression is easier than evaluating an infix expression because it does not contain any brackets
# and there are no operator precedence rules to consider.
# Write a program that reads a mathematical expression in infix form from the user, evaluates it, and displays its
# value. Uses your solutions to Exercises 122 and 123 along with the algorithm shown above to solve this problem.


def evaluate_infix(expression):
    from pwb_ex123 import infix_to_postfix
    # Tokenize expression and convert infix expression to postfix
    postfix_form = infix_to_postfix(expression)
    # Create a new empty list, values
    values = []
    # For each token in postfix expression
    for x in postfix_form:
        # If the token is a number then
        if "0" <= x <= "9":
            # Convert it to an integer and add it to the end of values
            values.append(int(x))
        else:
            # Remove an item from the end of values and call it right
            right = values.pop()
            # Remove an item from the end of values and call it left
            left = values.pop()
            # Apply the operator to left and right
            if x == "+":
                res = left + right
            if x == "-":
                res = left - right
            if x == "*":
                res = left * right
            if x == "/":
                res = left / right
            # Append the result to the end of values
            values.append(res)
    # Return the first item in values as the value of the expression
    return values[0]


# Main function demonstrates program performance
def main():
    # Prompts user to input the expression
    expression = input("Please enter your expression in infix form here: ")
    # display the value of the entered by user expression
    print("Your expression value is {}".format(evaluate_infix(expression)))


if __name__ == '__main__':
    main()
