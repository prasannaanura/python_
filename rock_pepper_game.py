import random

# Function to get user input
def get_user_choice():
    while True:
        user = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
        if user in ["rock", "paper", "scissors"]:
            return user
        elif user == "q":
            print("Thanks for playing! 🎉")
            exit()
        else:
            print("❌ Invalid choice! Try again.")

# Function to get computer choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Initialize score variables
user_score = 0
computer_score = 0
ties = 0

# Main game loop
while True:
    print("\n===== Rock, Paper, Scissors Game =====")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"🧑 You chose: {user_choice}")
    print(f"🤖 Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    # Update score based on the result
    if winner == "user":
        print("🎉 You win this round!")
        user_score += 1
    elif winner == "computer":
        print("😢 Computer wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a tie!")
        ties += 1

    # Display current scores
    print(f"\n🔢 **Current Score:**")
    print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score} | 🤝 Ties: {ties}")

    # Ask if the user wants to continue
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Final Score:")
        print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score} | 🤝 Ties: {ties}")
        break
