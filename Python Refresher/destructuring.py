x, y = (1, 2)  # x=1, y=2

people = [("Bob", 42, "Mechanic"), ("Sam", 32, "Magician"), ("Shyam", 28, "Astrologer")]

for name, age, job in people:
    print(f"Name: {name}, Age: {age}, Job: {job}")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Job: {person[2]}")

# ------------------------------------------------------------------------------------------

"""We can use _ as a variable. But Python community suggest don't use unless it required as variable"""

detail = ("Bob", 25, "Archeologist")
name, _, job = detail

print(name, job) # if you don't need Age parameter, then ypu can use _ as variable.

# ------------------------------------------------------------------------------------------

head, *tail = [1, 2, 3, 4, 5]  # head will take value 1 and maximum value will be assigned to tail
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]  # head will take maximum numbers and leaving 1 value (last value) to tail
print(*head)  # This will print without the list
print(tail)