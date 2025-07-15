#String basics
message = """Bob's World
is cool"""

#Advanced concepts - strings

message2 = " Hello, World! "

#python built-in functions

print(len(message2)) # Counts string characters including whitespaces if applicable
print(message2.strip()) # Removes leading and trailing whitespace
print(message2.lower()) # Conert all characters to lowercase
print(message2.split(',')) # Splits the string into a list based on the comma

print(message2.upper()) # Converts all characters into uppercase

# Advanced concepts Indexing,

message3 = "Hello"
print(message3[0])
print(message3[-1])