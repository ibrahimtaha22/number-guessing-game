import random

def get_user_input():
    """Ask the user for a number between 1 and 10, validating the input."""
    while True: 
        try:
            user_input = int(input("Please choose a number from 1 to 10: "))
            if 1 <= user_input <= 10: 
                return user_input
            else: 
                print("⚠️  The number is out of range, please try again!")
        except ValueError:
            print("❌ Invalid input! Please enter an integer number.")

def play_game():
    """Main game loop for the number guessing game."""
    attempts = 0 
    computer = random.randint(1, 10)
    print("\n🎮 The game starts — good luck!\n")

    while True: 
        user = get_user_input()
        attempts += 1
        print(f"🙎 Your guess: {user}\n")

        if user == computer: 
            print(f"🎉 Congratulations! You won on attempt #{attempts}.\n")
            break
        elif user < computer: 
            print("⬇️ Your guess is too low.\n")
        else:  # user > computer
            print("⬆️ Your guess is too high.\n")

def main():
    while True:
        play_game()
        again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
