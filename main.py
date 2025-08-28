""" Number Guess game """
import random
from art_vars import WELCOME_ART, WIN_ART, GAME_OVER_ART

def get_difficulty():
    """Get the difficulty level from the user."""
    print("\nChoose your difficulty level:")
    print("1. Easy (1-50, unlimited attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    print("4. Expert (1-500, 5 attempts)")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                return 1, 50, float('inf')  # min, max, max_attempts
            if choice == 2:
                return 1, 100, 10
            if choice == 3:
                return 1, 200, 7
            if choice == 4:
                return 1, 500, 5
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    """Play a number guessing game where the user tries to guess a random number."""
    min_num, max_num, max_attempts = get_difficulty()
    number_to_guess = random.randint(min_num, max_num)
    attempts = 0

    print(f"\nGreat! I'm thinking of a number between {min_num} and {max_num}.")
    if max_attempts != float('inf'):
        print(f"You have {max_attempts} attempts to guess it!")
    else:
        print("You have unlimited attempts!")

    while True:
        try:
            user_guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            attempts += 1

            if user_guess == number_to_guess:
                print(WIN_ART)
                print(f"You've guessed the number in {attempts} attempts.")
                break
            if user_guess < number_to_guess:
                print("📈 Too low! Try again.")
            else:
                print("📉 Too high! Try again.")

            # Check if maximum attempts reached
            if attempts >= max_attempts:
                print(GAME_OVER_ART)
                print(f"You've used all {max_attempts} attempts.")
                print(f"The number was {number_to_guess}. Better luck next time!")
                break
            if max_attempts != float('inf'):
                remaining = max_attempts - attempts
                print(f"Attempts remaining: {remaining}")

        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main game loop with replay option."""
    print(WELCOME_ART)

    while True:
        play_game()

        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                break
            if play_again in ['n', 'no']:
                print("Thanks for playing! Goodbye! 👋")
                return
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()

