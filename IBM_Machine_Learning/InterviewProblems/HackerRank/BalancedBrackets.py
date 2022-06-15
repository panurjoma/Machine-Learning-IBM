"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of
 a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is
not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single,
unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

Some examples of balanced brackets are []{}(), [({})]{}() and ({(){}[]})[].
By this logic, we say a sequence of brackets is considered to be balanced if the following conditions are met:
It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print
YES on a new line; otherwise, print NO on a new line.

Function Description
Complete the isBalanced function in the editor below.
isBalanced has the following parameter(s):
- string expression: a string of brackets
Returns
- string: either YES or NO
Input Format
The first line contains a single integer, , the number of strings.
Each line  of the  subsequent lines consists of a single string, , denoting a sequence of brackets.
"""


# Recursive option
def isBalanced1(expression):
    # Write your code here
    if expression == None or len(expression) == 0:
        return "YES"
    is_balanced = "NO"
    if expression[0] == "{":
        for index in range(len(expression)):
            if (expression[index] == "}"):
                if (isBalanced(expression[1:index]) == "YES" and
                                    isBalanced(expression[(index + 1):]) == "YES" ):
                                    is_balanced = "YES"
    elif expression[0] == "[":
        for index in range(len(expression)):
            if (expression[index] == "]"):
                if (isBalanced(expression[1:index]) == "YES" and
                                    isBalanced(expression[(index + 1):]) == "YES" ):
                                    is_balanced = "YES"
    elif expression[0] == "(":
        for index in range(len(expression)):
            if (expression[index] == ")"):
                if (isBalanced(expression[1:index]) == "YES" and
                                    isBalanced(expression[(index + 1):]) == "YES" ):
                                    is_balanced = "YES"

    return is_balanced

# Non-recursive option
def isBalanced2(expression):
    # Write your code here
    if expression == None or len(expression) == 0:
        return "YES"
    if expression[0] == "]" or expression[0] == ")" or expression[0] == "}":
        return "NO"
    is_balanced = "YES"
    top = None
    stack = []
    # initialize
    top = expression[0]
    stack.append(top)

    expression = expression[1:]
    for index, char in enumerate(expression):
        stack.append(char)
        if (top == "{" and stack[-1] == "}") or \
                (top == "[" and stack[-1] == "]") or \
                (top == "(" and stack[-1] == ")"):
            stack.pop()
            stack.pop()
            if (len(stack) != 0):
                top = stack[-1]
            else:
                top = None
        elif (top == "{" and (stack[-1] == "]" or stack[-1] == ")")) or \
                (top == "[" and (stack[-1] == "}" or stack[-1] == ")")) or \
                (top == "(" and (stack[-1] == "]" or stack[-1] == "}")):
            is_balanced = "NO"
            break
        else:
            top = char

    if len(stack) != 0:
        is_balanced = "NO"

    return is_balanced

bracket_expression = "{[()]}"
is_balanced = isBalanced2(bracket_expression)
print(is_balanced)

