#4th August 2026
#basics function code
"""
# a function that receives a number and returns the square


def squared(value):
    return value * value

square=int(input("Enter your value: "))
print("The square is : ",squared(square))

"""
"""
#a function that receives a persons name and returns a greeting

def greeting(name):
    return name

user_input=input("What's your name? ")
print("Welcome, ",greeting(user_input))
"""

# a function that receives three values and return the average
def averages(num1,num2,num3):
    return (num1+num2+num3)/3

input1= int(input("Input Num1 "))
input2= int(input("Input Num2 "))
input3= int(input("Input Num3 "))
print("The Average is ",averages(input1,input2,input3))
