students = []

def result(marks):
    total = sum(marks.values())
    percentage = total / 3

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


for i in range(5):
    print("\nStudent", i + 1)
    name = input("Name: ")
    roll = input("Roll: ")

    marks = {
        "Python": float(input("Python marks: ")),
        "AI": float(input("AI marks: ")),
        "Math": float(input("Math marks: "))
    }

    total, percentage, grade = result(marks)
    students.append([name, roll, total, percentage, grade])

for student in students:
    print(student)

highest = max(students, key=lambda x: x[3])
print("Highest:", highest)

with open("results.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write(str(student) + "\n")
    file.write("Highest: " + str(highest))
