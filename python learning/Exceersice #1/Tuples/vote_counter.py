# Exercise 9: Vote counter
# votes = ("A", "B", "A", "C", "A", "B")
# Use count() to count the votes for A, B and C, and index() to find the position of the first
# "C".
# Expected: A=3 B=2 C=1, first C at index 3

votes = ("A", "B", "A", "C", "A", "B")

print(votes.count("A"))
print(votes.count("B"))
print(votes.count("C"))


vote_A = votes.count("A")
vote_B = votes.count("B")
vote_C = votes.count("C")

# first find the postion of c

c = votes.index("C")

print(f"A={vote_A}, B={vote_B}, C={vote_C}")
print(f"First C at index {c}")
