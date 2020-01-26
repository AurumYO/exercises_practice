# Exercise 123: Infix to Postfix (62 Lines)
# Mathematical expressions often written in infix form, where operators appear between the operands on which they act.
# While this is a common form, it is also possible to express mathematical expressions in postfix form, where the
# operator appears after both operands. For example, the infix expression 3 + 4 is written as 3 4 + in postfix form.

# Use your solution to Exercise 122 to tokenize a mathematical expression. Then use the algorithm above to transform
# the expression from infix form to postfix form. Your code that implements the preceding algorithm should reside
# in a function that takes a list of tokens representing an infix expression as its only parameter.


# this function converts an infix expression to postfix form using the algorithm:
def infix_to_postfix(string):
    # import tokenizer function from ex 122
    from pwb_ex122 import tokenizer
    # run tokenizer function to tokenize a mathematical expression
    tokenized_string = tokenizer(string)
    # Create a new empty list postfix, Create a new empty list operators
    postfix, operators = [], []
    operator = {"+", "-", ">", "<", "**", "*", "/", "//", "%" "^"}
    # for each token in the infix expression
    for s in tokenized_string:
        # If the token is an integer then
        if s.isdigit():
            # Add the token to the end of postfix
            postfix.append(s)
        # If the token is an operator then
        if s in operator:
            # While operators is not empty and the last item in operators is not an open parenthesis and
            # precedence(token) < precedence(last item in operators) do
            while len(operators) != 0 and operators[-1] != '(' and s < operators[-1]:
                # Remove the last item from operators and add it to postfix
                extracted_operator = operators.pop()
                postfix.append(extracted_operator)
            # Add token to the end of operator
            operators.append(s)
        # If the token is an open parenthesis then
        if s == '(':
            # Add token to the end of operators
            operators.append(s)
        # If the token is a close parenthesis then
        if s == ')':
            # While the last item in operators is not an open parenthesis do
            while operators[-1] != '(':
                # Remove the last item from operators and add it to postfix
                extracted_operator = operators.pop()
                postfix.append(extracted_operator)
            # Remove the open parenthesis from operators
            operators.remove('(')

    # While operators is not the empty list do
    while len(operators) != 0:
        # Remove the last item from operators and add it to postfix
        extracted_operator = operators.pop()
        postfix.append(extracted_operator)
    # Return postfix as the result of the algorithm
    return postfix


# main function demonstrates infix to postfix function by reading an expression from the user in infix form
# and displaying it in postfix form.
def main():
    st = input("Please enter your string here: ")
    res = infix_to_postfix(st)
    print("Your math string in postfix form is: ")
    # representing expression in postfix form as string
    outcome = ''.join(x + " " for x in res)
    print(outcome)


if __name__ == '__main__':
    main()
