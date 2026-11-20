# Make a = [1, 2, 3], then b = a and c = a.copy(). Append 4 to a, then print a, b and
# c. In a comment, explain why b changed but c did not.


a = [1,2,3]
b =  a
c = a.copy()

a.append(4)

print(a)
print(b)
print(c)

# because b is shallow copy( in it if we change the original one it also chage in its copy)
# while c is not change becuse it is a deep copy and in deep copy the original change or not the copy does not take any affect from original one

