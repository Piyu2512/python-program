# conditions

# Check whether a number is positive, negative, or zero

num = -10

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
    

# Check whether a person is eligible to vote

age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    

# Find the largest of three numbers

a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# Check whether a year is a leap year

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# Grade System Based on Marks

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Marks:", marks)
print("Grade:", grade)


# Check whether a number is divisible by 5 and 11

num = 55

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11")
else:
    print("Number is not divisible by both 5 and 11")


# Simple Calculator

a = 10
b = 5
operator = "+"

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

