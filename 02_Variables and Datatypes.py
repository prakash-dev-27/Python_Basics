# Python Variables
# Topic: Storing and using data

# Creating variables
name = "Python Learner"
age = 22
height = 5.8
is_learning_python = True

# Displaying variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", is_learning_python)

# Updating a variable
age = 23
print("Updated age:", age)

# Using variables in calculations
number1 = 10
number2 = 20

total = number1 + number2

print("First number:", number1)
print("Second number:", number2)
print("Total:", total)

Output: 

Name: Python Learner
Age: 22
Height: 5.8
Learning Python: True
Updated age: 23
First number: 10
Second number: 20
Total: 30

Datatypes:

# Integer
age       = 25
year      = 2024
negative  = -10

# Float
pi        = 3.14159
price     = 19.99
gpa       = 3.75

# String
name      = "Alice"
greeting  = 'Hello, World!'
multiline = """This spans
multiple lines"""

# Boolean
is_raining    = True
has_completed = False

# None
result = None

# Check type with type()
print(type(age))        # <class 'int'>
print(type(pi))         # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_raining)) # <class 'bool'>
print(type(result))     # <class 'NoneType'>

# isinstance() — check if variable is a specific type
print(isinstance(age, int))    # True
print(isinstance(pi, float))  # True
print(isinstance(name, str))  # True

# id() shows where in memory the value lives
x = 10
print(id(x))   # memory address (number)

y = x          # y points to the SAME object as x
print(id(y))   # same as id(x)!

x = 20         # now x points to a new object
print(id(x))   # different address now
print(id(y))   # y still points to original 10
