number = 7
user_num = input("Select Y if you are ready: ").lower()

if user_num == "y":
    
    user_val = int(input("Enter the Guessed Magic Number: "))

    if user_val == number:
        print("You guessed correctly")

    elif abs(user_val - number) == 1:   # abs() will give absolute value. abs(-1) = 1
        print("You were off by one.")   # Alternate: elif user_val - number in (1, -1)

    else:
        print("Sorry its wrong!")