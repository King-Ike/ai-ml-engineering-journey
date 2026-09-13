#6th August 2026


"""
program 1
Create a function called Grade that
Return:
A if 70+
B if 60–69
C if 50–59
F below 50
Remember:
No input() inside the function."""

"""
def grade(score):
    if score >= 70: 
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "f"
x = int(input("input your score "))
print(grade(x))"""

"""
#program 2
#Question 2

#Create a function that receive 3 inputs and return the biggest 

def largest(a,b,c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c
x = int(input("input value for A "))
y = int(input("input value for B "))
z = int(input("input value for C "))
print("the largest value is", largest(x, y, z))

"""

#program3
#Create a function called discount that 
#If the price is above ₦50,000,
#return the price after a 10% discount.
#Otherwise,
#return the original price.


def discount(price):
     if price > 50000:
        return price - (price * 0.1)
     else:
        return price
x = int(input ("input your price "))
print("your discounted price is", discount (x))


