# prompts user to enter score
score = int(input("Pick a number between 1-100:"))

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
# elif score <= 59:
#     grade = "F"
else:
    grade = "F"

print (f"the grade for score {score} is {grade}")
