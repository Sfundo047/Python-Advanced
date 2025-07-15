#Loops [for]

fruits = ["Apples", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)

print() # adds line space in the console
numbers = [1, 2, 3, 5, 7]

for number in numbers:
    print(number)
    
print() # adds line space in the console
#Loop control statements

fruits = ["Apples", "Banana", "Cherry", "date"]

for fruit in fruits:
    if fruit == "Cherry":
        break # Exits the loop if Cherry is found
    print(fruit)

print()
  
for fruit in fruits:
    if fruit == "Cherry":
        continue # Skips Cherry and moves to the next iteration
    print(fruit)

print()

for fruit in fruits:
    if fruit == "Cherry":
       pass # Placeholder, no action is needed for cherry
    print(fruit)