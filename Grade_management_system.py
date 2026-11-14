
print("Let's see students' performance")
students = {
    'Ravi': {'python': 78, 'sql': 100, 'Maths': 98},
    'Ram': {'python': 98, 'sql': 45, 'Maths': 98},
    'Abi': {'python': 68, 'sql': 80, 'Maths': 78},
    'Samya': {'python': 98, 'sql': 89, 'Maths': 98},
    'Resmi': {'python': 100, 'sql': 35, 'Maths': 67}
}
def student(name):
    if name not in students:
        return "Student not found!"
    total = 0
    for marks in students[name].values():
        total += marks
    average = total / len(students[name])
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F - Needs improvement"
    # highest = 0
    # topper = ""
    # for student_name, marks in students.items():
    #     student_total = sum(marks.values())
    #     if student_total > highest:
    #         highest = student_total
    #         topper = student_name
    return (
        f"Student Name: {name}\n"
        f"Subject Marks: {students[name]}\n"
        f"Total: {total}\n"
        f"Average: {average:.2f}\n"
        f"Grade: {grade}\n\n"
        # f"Class Topper: {topper}\n"
        # f"Highest Marks: {highest}"
    )
name = input("Enter student name: ")
print(student(name))
