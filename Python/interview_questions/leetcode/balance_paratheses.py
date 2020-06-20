"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

def balance_parantheses(expr):
    stack = []
    match = { ")":"(", "}":"{", "]":"[" }
    for char in expr:
        if char in "[{(":
            stack.append(char)
        else:
            if not stack:
                return False
            if match[char] != stack[-1]:
                return False
            else:
                stack.pop()
        if len(stack) == 0:
            return True
    return False
print(balance_parantheses("[{()}]"))
