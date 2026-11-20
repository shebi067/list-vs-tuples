# Exercise 4: Remove duplicates
# nums = [3, 1, 3, 2, 1, 5]
# Make a new list without duplicates, keeping the original order. Use a loop and not in, not
# set().



nums = [3, 1, 3, 2, 1, 5]

new_nums = []

for n in nums:
    if n not in new_nums:
        new_nums.append(n)
        print("Unique Number: ", new_nums)
        