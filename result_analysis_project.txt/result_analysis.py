
import pandas as pd

questions = pd.read_excel("Questions.xlsx")
responses = pd.read_excel("Student_Responses.xlsx")

answer_key = {}
for _, row in questions.iterrows():
    answer_key[f"Q{row['Q.No']}"] = row["Correct Answer"]

for _, student in responses.iterrows():
    correct = 0
    total = len(answer_key)

    for q, ans in answer_key.items():
        if student[q] == ans:
            correct += 1

    percentage = (correct / total) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"Student: {student['Name']}")
    print(f"Correct Answers: {correct}/{total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("-" * 30)
