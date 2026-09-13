#7th August 2026

"""
#Program 1
# create a program that returns "VALID" if all three sides can create a Triangle Else "INVALID"


def is_triangle(a,b,c) :
     if (a + b> c) and (a + c > b) and (b + c > a):
        return "Valid"
     else:
        return "Invalid"
x = int(input("input value for A "))
y= int(input("input value for B "))
z = int(input("input value for C "))
print(is_triangle(x, y, z))
"""
"""
#program 2
#mini password validator

def pass_strength(password) :
       if password < 8: 
           return "Weak"
       else:
          return "Strong"
x=int (len(input ("what's your password? ")))
print(pass_strength(x))
"""

#program 3
#mini ai confidence predictor


def classify_sign (confidence):
    if confidence >= 90: 
        return "Recognized" 
    elif confidence >= 70:
        return "needs Confirmation"
    else:
       return "unknown"
x = int(input("input a value to predict "))
print(classify_sign(x))
