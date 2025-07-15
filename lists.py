#lists can be strings, numeric data or other lists
#Python lists are zero indexed

fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])

fruits[1] = "Blueberry"

print(fruits[1])

print()

# Adding & removing items in a list

fruits2 = ["Apple", "Banana", "Cherry"]

fruits2.append("Kiwi")
print(fruits2)

fruits2.insert(1, "Orange")
print(fruits2)

fruits2.remove("Kiwi")
print(fruits2)

fruits2.sort()
print(fruits2)

fruits2.sort(reverse= True)
print(fruits2)