The naming system and storage mechanism behind every Python program.

Identifiers — Names You Create

#  Valid identifiers
student_name = "Alice"
_private_var = 42
myVariable   = "hello"
count1       = 0

#  Invalid identifiers
# 1name = "bad"     → cannot start with a digit
# my-var = "bad"    → hyphens not allowed
# for = 10          → reserved keyword

# Case sensitivity: these are 3 DIFFERENT variables!
score = 90
Score = 80
SCORE = 70
print(score, Score, SCORE)  # prints: 90 80 70

Keywords — Python's Reserved Words

import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
#  'except', 'finally', 'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
#  'return', 'try', 'while', 'with', 'yield']

print(len(keyword.kwlist))  # 35 keywords in Python 3

Comments — Notes for Humans

# Single-line comment — starts with #
x = 10  # inline comment after code

"""
Multi-line comment using triple quotes.
Often used at the start of a function or file
to explain what the code does.
This is also called a docstring.
"""

'''
You can also use single triple-quotes.
Both are equivalent.
