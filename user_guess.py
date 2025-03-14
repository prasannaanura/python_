import random

# Take input and validate it
top_of_range = input("Enter a number between 1 and 10: ")

if top_of_range.isdigit():  # Check if input is a number
    top_of_range = int(top_of_range)
    if 1 <= top_of_range <= 11:  # Ensure it's within the valid range
        random_num = random.randint(1, top_of_range)  # Generate a random number
    else:
        print("Please enter a number between 1 and 10.")
        exit()
else:
    print("Invalid input! Please enter a numeric value.")
    exit()

guess = 0

while True:
    guess += 1
    user_guess = input("Enter your guess between 1 and 10: ")

    if user_guess.isdigit():  # Check if input is a number
        number = int(user_guess)
        if 1 <= number <= 11:  # Ensure it's within the valid range
            if number == random_num:
                print(f"Congratulations! You guessed the number\'{random_num}\' in {guess} attempts.")
                #break  # Exit loop
                break
            else:
                if number > random_num:
                    print("your guess too high!")
                else:
                    print("your guess too below")
        else:
            print("Please enter a valid number between 1 and 10.")
    else:
        print("Invalid input! Please enter a number.")
