# Exercise 8: Student record
# student = ("BSIT-12", "Sara", 88)
# 1. Unpack it into roll_no, name, marks and print each one with an f-string.
# 2. Try student[2] = 95 and write down the error you get.
# 3. Now update the marks the correct way: convert the tuple to a list, change the marks,
# then convert it back to a tuple.
# Expected: ('BSIT-12', 'Sara', 95)
 
student = ("BSIT-12", "Sara", 88)

roll_no, name, mark = student # variable assignment from right to left
print(f"roll no: {roll_no}")
print(f"Name: {name}")
print(f"Marks: {mark}")

# student[2] =95 
#TypeError: 'tuple' object does not support item assignment (beacuse tuples are immutable so we change the value by converting tuples into lists)

# updating the marks by converting

lists = list(student) # using list function for converting 
lists[2] = 95

student = tuple(lists) # reconverting

print(student)
