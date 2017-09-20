

score = float(input("Score: "))

def grade(score):
    if score >= 90:
        LetterGrade = "A"
    elif score >= 80:
        LetterGrade = "B"
    elif score >= 70:
        LetterGrade = "C"
    elif score >= 60:
        LetterGrade = "D"
    else:
        LetterGrade = "F"
    return LetterGrade

print(grade(score))