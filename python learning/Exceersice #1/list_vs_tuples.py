# lists
#ex 1
cities = ["ISB", "BWP","MUX", "KHI", "LHR"]

print(cities[0])
print(cities[-1])
print(cities[1:4])

cities.reverse()
print(cities)

# Ex 2

marks = [78, 92, 65, 88, 54]
Total_marks = sum(marks)
print(Total_marks) 

high = max(marks)
print(high)
low= min(marks)
print(low)

# average = Total_marks / marks
# print(average) 



# ex 3

shopping = ["bread", "milk", "eggs"]
shopping.append("Egggsss")
print(shopping)

shopping.pop()
shopping.remove("milk")
print(shopping)
shopping.insert(1, "juice")
print(shopping)


# ex 4

nums = [3, 1, 3, 2, 1, 5]

new_nums = [2,3,1,5,3,1,6]

print([num for num in nums if num in new_nums])

# ex 5

even_odd = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]



even = ([num for num in even_odd if num % 2 == 0])

print(even)

odd = ([num for num in even_odd if num % 2!=0])

print(odd)

# ex 6

r = [1, 2, 3, 4, 5]
r[0:2] = r[2:4]
print(r)



# ex 7

a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print(a)
print(b)
print(c)
# b is not changed because it's a shallow copy and c is a deep copy of a

# ex 8

student = ("BSIT-12", "Sara", 88)






# Level 3: Tuples
# Exercise 8: Student record
# student = ("BSIT-12", "Sara", 88)
# 1. Unpack it into roll_no, name, marks and print each one with an f-string.
# 2. Try student[2] = 95 and write down the error you get.
# 3. Now update the marks the correct way: convert the tuple to a list, change the marks,
# then convert it back to a tuple.
# Expected: ('BSIT-12', 'Sara', 95)
# Exercise 9: Vote counter
# votes = ("A", "B", "A", "C", "A", "B")
# Use count() to count the votes for A, B and C, and index() to find the position of the first
# "C".
# Expected: A=3 B=2 C=1, first C at index 3
# Exercise 10: List of tuples
# students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]
# 1. Loop through the list and print each student as Ali scored 85.
# 2. Find the topper.
# 3. Make a list of the names of students who passed (marks 70 or above).
# Expected: topper Sara 92, passed ['Ali', 'Sara', 'Ahmed']
# Challenge
# Exercise 11: Second highest
# scores = [45, 82, 67, 91, 73]
# Find the second highest score with a loop only. Don't use sort() or max().
# Expected: 82
