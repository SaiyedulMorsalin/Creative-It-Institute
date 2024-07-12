'''
Python divides the operators in the following groups:
    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators 
'''
# Arithmetic Operators (+,-,*,/,%,**,//)
number1 = 10
number2 = 5
print(f"Number1 + Number2 = {number1+number2}")
print(f"Number1 - Number2 = {number1-number2}")
print(f"Number1 * Number2 = {number1*number2}")
print(f"Number1 % Number2 = {number1%number2}")
print(f"Number1 ** Number2 = {number1**number2}")
print(f"Number1 // Number2 = {number1//number2}")
# Assignment Operators(=,+=,-=,*=,/=,%=,**=,)
a = 10 # assignment operator
b = 20
a+=b
print("Addition Assignment of a = ",a)
a-=b
print("Subtraction Assignment of a = ",a)
a*=b
print("Multiplication Assignment of a = ",a)
a/=b
print("Division Assignment of a = ",a)
a%=b
print("Reminder Assignment of a = ",a)
a**=b
print("Exponent Assignment of a = ",a)
# Comparison Operators(==,!=,>,<,>=,<=)
a = 5
b = 2
print('a == b =', a == b)
print('a != b =', a != b)
print('a > b =', a > b)
print('a < b =', a < b)
print('a >= b =', a >= b)
print('a <= b =', a <= b)
# Logical Operators(and,or,not)
print(True and True)     # True  
print(True and False)    # False  (jekono ekti false hole false return korbe)
print(True or False)     # True   (jekono ekti true hole true return korbe)
print(not True)          # False  
# Identity Operators(is,is not)
x,y = 5,3
print(x is y) # False
print(x is not y) # True
# Membership Operators(in, not in)
institute = 'Creative IT Institute'
# check if 'IT' is present in institute string
print('IT' in institute) # True
print("CIT" in institute) # Flase
print("CIT" not in institute) # True 