# Exercise 10: List of tuples
# students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]
# 1. Loop through the list and print each student as Ali scored 85.
# 2. Find the topper.
# 3. Make a list of the names of students who passed (marks 70 or above).
# Expected: topper Sara 92, passed ['Ali', 'Sara', 'Ahmed']


students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]
# using loop through the list
for name, marks in students:
    print(f"{name} score {marks}")

topper_name = students[0][0] # these two 0s index the first tuple (ali, 85) first index ne tuple nikala aur dosry tuple ne tuple ke andar first index jo ke name h ali 
topper_marks = students[0][1] # ab yaha pr first 0 pehla tuple nikala aur aur 1 index ne usky marks

for name, marks in students:
    if marks > topper_marks: # yaha pr jab loop chla aur sara ke marks zyada thy ali se aur baqi sab se tum usko topper decalred krdiya gaya
        topper_marks = marks
        topper_name = name

passed = []

for name, marks in students:
    if marks>=70:
        passed.append(name) # ab yaha pr jo baqi ke reh gaye thy unke liye function use kiya append aur add krdiya with loop

print(f"topper {topper_name}{topper_marks}, pass {passed}")

