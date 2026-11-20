# Exercise 11: Second highest
# scores = [45, 82, 67, 91, 73]
# Find the second highest score with a loop only. Don't use sort() or max().
# Expected: 82


scores = [45, 82, 67, 91, 73]

# pehly du variable banay pryngy

highest = 0
second_highest = 0 

for score in scores:
    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest and score !=highest:
        second_highest = score

print("second highest score is: ", second_highest)





