
# r = [1, 2, 3, 4, 5]
# Use slicing only to move the first two items to the end.
# Expected: [3, 4, 5, 1, 2]


r = [1, 2, 3, 4, 5]
r = r[2:] + r[:2]
print(r)
