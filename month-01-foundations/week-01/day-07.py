#9th August 2026
"""
#program 1


def even_or_odd (number):
    if number % 2 == 0: 
        return "Even"
    else:
        return "odd"
x = int(input("Input Your Number "))
print(even_or_odd(x))
"""

"""
#program 2
# a program that returns the largest number out of all input

def largest(a, b,c):
    if (a>=c) and (a>=b):
        return "A is the Largest"
    elif (b>=a) and (b>=c):
        return "B is the Largest"
    else:
        return "C is the Largest"
x=int (input("Input Your Value For A "))
y=int (input("Input Your Value For B "))
z=int (input ("Input Your Value For C "))
print(largest(x,y,z))
"""

#program 3
#mini ai confidence checker

def classify_confidence(confidence) :
     if 90 <=confidence <=100:
         return "High Confidence" 
     elif 70<= confidence <=89:
          return "Medium Confidence"
     elif 0<= confidence <=69: 
          return "Low Confidence"
     else:
          return "Invalid"
x=int(input ("Input Your Confidence Value "))
print(classify_confidence(x))
