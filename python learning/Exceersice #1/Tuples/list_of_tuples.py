# Exercise 10: List of tuples
# students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]
# 1. Loop through the list and print each student as Ali scored 85.
# 2. Find the topper.
# 3. Make a list of the names of students who passed (marks 70 or above).
# Expected: topper Sara 92, passed ['Ali', 'Sara', 'Ahmed']


students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]

for name, marks in students:
    print(f"{name} score {marks}")


topper_name = students[0][0]
topper_marks = students[0][1]

for name, marks in students:
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

passed = []

for name, marks in students:
    if marks>=70:
        passed.append(name)

print(f"topper {topper_name}{topper_marks}, pass {passed}")