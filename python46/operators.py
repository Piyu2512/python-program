# operators

# Perform Addition, Subtraction, Multiplication and Division

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Find quotient and remainder

a = 17
b = 5

quotient = a // b
remainder = a % b

print("Quotient:", quotient)
print("Remainder:", remainder)

# Check whether a number is even or odd

num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Compare two numbers using relational operators

a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Demonstrate Logical Operators

a = 10
b = 20

print("AND:", a > 5 and b > 15)
print("OR:", a > 15 or b > 15)
print("NOT:", not(a > 5))


# Demonstrate Assignment Operators

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)


# Find the largest of two numbers

a = 25
b = 40

if a > b:
    print("Largest number:", a)
else:
    print("Largest number:", b)

