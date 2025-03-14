import random

# Get user input and convert it to an integer
top_num = int(input("Enter a number: "))

# Generate a random number between 1 and top_num
random_num = random.randint(1,top_num)

print(f"Random number between 1 and {top_num}: {random_num}")
