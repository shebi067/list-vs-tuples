
# marks = [78, 92, 65, 88, 54]
# Print the total, the average, the highest, the lowest, and how many marks are above 70 (use a
# loop).


marks = [78, 92, 65, 88, 54]
Total_marks = sum(marks)
print(Total_marks) 

high = max(marks)
print(high)
low= min(marks)
print(low)

average = Total_marks / len(marks)
print(average) 


above =[]

for n in marks:
    if n>70:
        above.append(n)
        print(above)

