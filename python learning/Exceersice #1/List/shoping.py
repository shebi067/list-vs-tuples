# Start with ["bread", "milk", "eggs"]. Then:
# ● append "rice"
# ● insert "sugar" at index 1
# ● remove "milk"
# ● pop() the last item and print what was popped



shopping = ["bread", "milk", "eggs"]
shopping.append("rice")
print(shopping)

shopping.pop()
shopping.remove("milk")
print(shopping)
shopping.insert(1, "sugar")
print(shopping)
