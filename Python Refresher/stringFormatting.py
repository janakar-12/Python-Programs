"""String Formatting"""

name = "Avinash"
print(f"Hello {name}!")

name = "Tyson"
print(f"Hello {name}!")

# ------------------------

"""Formatting Template"""

msg = "Hello, {}. Today is {}"  #  This will act as template

formatted = msg.format("Avinash", "Sunday") #  This format will place the value in above placeholder

print(formatted)