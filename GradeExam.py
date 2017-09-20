
'''
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

print(grade(score))'''

grade=int(input("Score: "))
gradeKey={9:"A", 8:"B", 7:"C", 6:"D", 5:"F", 4:"F", 3:"F", 2:"F", 1:"F", 0:"F"}
print(gradeKey[int(grade/10)])