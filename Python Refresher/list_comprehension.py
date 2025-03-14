"""We have list with numbers. We need to double the value and to store in another list"""

numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]

# print(doubled)
# ------------------------------------------------------------------------------------------

"""To get the name starts with letter S"""

names = ["Jack", "Sparrow", "Ben", "Scorpian", "Cerberus", "Sam"]
s_name = [x for x in names if x.startswith("S")]

# print(s_name)

print(f"names: {id(names)}, s_name: {id(s_name)}")  # To print the memory address of the list