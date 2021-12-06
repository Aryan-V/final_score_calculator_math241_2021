"""
Developed by: Aryan Vaswani
For use with UIUC Math 241, Fall 2021

https://github.com/Aryan-V/final_score_calculator_math241_2021
"""

# This calculator determines what score you would need on the Math 241 Final Exam
# to earn a grade between all possible GPA brackets at UIUC.
# The only part of the code needed to be changed is below
# If being used with a different semester, modify the curves section

# enter the percent of your grade lost in the HW, Worksheets, and Quizzes categories
totalpercentlost = 0.1

# raw first exam score
score1 = 41

# raw second exam score
score2 = 41

# raw third exam score
score3 = 41

# raw fourth exam score (if not taken yet then input expected score)
score4 = 0

# which exam number you plan on dropping
drop = 4

# CURVES
# DO NOT MODIFY THE FOLLOWING CODE UNLESS FOR A DIFFERENT SEMESTER THAN FALL 2021
# COMPUTED BY SUBTRACTING THE RANGE OF POINT VALUES ASSOCIATED WITH AN A, B, C, D, OR F
# E.G. IF 39.5 - 45 IS AN A, THEN THE FIRST VALUE WOULD BE 5.5
# CONTINUE IN THIS ORDER THROUGH THE LIST
curve1 = [5.5, 7.4, 6.9, 5.9, 18.9]
curve2 = [4.5, 4.4, 4.4, 4.4, 26.9]
curve3 = [6, 9.9, 7.9, 5.9, 14.9]


# DO NOT MODIFY THE FOLLOWING CODE
def curve_exam(score, exam):
    if exam == 1:
        curve = curve1
    elif exam == 2:
        curve = curve2
    else:
        curve = curve3

    ranges = []
    max = 45
    for num in range(len(curve) - 1):
        ranges.append(round(max - curve[num], ndigits=1))
        max -= (curve[num] + 0.1)

    ranges.append(0)

    gradeRange = 0
    delta = 0
    sum = 0

    for letter in range(len(ranges) - 1, -1, -1):
        if sum <= score <= (sum + curve[letter]):
            gradeRange = letter
            delta = score - sum
        sum += curve[letter] + 0.1

    if gradeRange < 4:
        denom = curve[gradeRange] / 10
    else:
        denom = curve[gradeRange] / 60

    curvedpercent = delta/denom

    maxScore = 100
    for x in range(len(ranges)):
        if x == len(ranges) - 1:
            maxScore -= 60
        else:
            maxScore -= 10
        if score >= ranges[x]:
            curvedpercent += maxScore
            break

    return curvedpercent


scores = [score1, score2, score3, score4]
sum = 0

for nums in range(len(scores)):
    scores[nums] = curve_exam(scores[nums], nums + 1)

scores.pop(drop - 1)

for o in range(len(scores)):
    sum += scores[o]

sum = ((sum/3) * 0.56)
grade = [93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60]
for x in range(len(grade)):
    desiredgrade = grade[x]
    print("Final Exam Score Needed for a " + str(desiredgrade) + "%: " + str(round((desiredgrade
          - (20 + sum - totalpercentlost)) / 24 * 100, ndigits=2)) + "%.")
