#8th August 2026
#mini Grader


def calc_grade(score):
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60 and score <= 69:
       return "B"
    elif score >= 50 and score <= 59:
        return "C"
    elif score >= 45 and score <=49:
        return "D"
    elif score >= 0 and score <= 44:
        return "F"
    else:
        return "invalid value"
x = int(input("input your score "))
print(calc_grade(x))


