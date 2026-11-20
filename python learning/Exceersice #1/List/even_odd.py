# Exercise 5: Even and odd
# Using list comprehension, make two lists from the numbers 1 to 15: one with the even numbers
# and one with the odd numbers.

even_odd = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]



even = ([num for num in even_odd if num % 2 == 0])

print(even)

odd = ([num for num in even_odd if num % 2!=0])

print(odd)