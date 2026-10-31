#Statements
A statement is a complete instruction that Python can execute. Every line of Python code that does something is a statement.

# 1. Assignment Statement — store a value
x = 10
name = "Alice"

# 2. Print Statement — display output
print("Hello, World!")

# 3. Conditional Statement — make a decision
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
  
# with break
for i in range(1, 6):
    if i == 3:
        break
    print(i)

Output:  
1
2

#with continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:
1
2
4
5

Break            	    Continue
Stops the loop	      Skips current iteration
Loop terminates	      Loop continues
Used to exit a loop	  Used to skip an iteration


# 4. Loop Statement — repeat actions
for i in range(5):
    print(i)
 
#Import Statement  

The import statement is used to include modules in your Python program.
A module is a file containing reusable Python code.

Example: 
import math  --import math imports the math module.

print(math.sqrt(25))
print(math.pi)

#Return Statement 
  
The return statement is used inside a function to send a result back to the place where the function was called.

Example:
def add(a, b):   --The function add() receives two values.
    result = a + b
    return result

answer = add(10, 20)

print(answer)

#Compound Statements
Compound statements contain multiple statements grouped together.
They usually use a colon (:) and indentation.

A. If Statement
The if statement is used for decision-making.

Example:
age = 20

if age >= 18:
    print("You are eligible to vote")

Output:
You are eligible to vote

B.If-Else Statement
The else statement executes when the if condition is false.

age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

Output:
Not eligible to vote

C. Elif Statemen

elif means "else if".
It is used when you need to check multiple conditions.

Example:
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

Output:
Grade B

For Loop Statement
A for loop is used to repeat a block of code for each item in a sequence.
Example:
for i in range(1, 6):    --range(1, 6) generates numbers from 1 to 5.  --for i takes each number one by one.
    print(i)

While Loop Statement
A while loop executes as long as a condition is true.
Example:
count = 1

while count <= 5:
    print(count)
    count = count + 1

Explanation:
1. Initially, count = 1.
2. Python checks count <= 5.
3. If true, it prints the value.
4. It increases the count by 1.
5. This continues until the condition becomes false.

Function Definition Statement
The def keyword is used to create a function.

Example:
def greet():
    print("Hello")
    print("Welcome to Python")

greet()

Output:
Hello
Welcome to Python

Explanation:
- def greet(): defines the function.
- The indented lines belong to the function.
- greet() calls and executes the function.

Class Definition Statement
A class statement is used to create a class in Python.
A class is a blueprint for creating objects.

Example:
class Student:
    name = "Prakash"
    age = 25

student1 = Student()

print(student1.name)
print(student1.age)

Practical Example – Student Marks Calculator

# Student details
name = "Prakash"
marks = 85

# Display student details
print("Student Name:", name)
print("Marks:", marks)

# Check the grade
if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
