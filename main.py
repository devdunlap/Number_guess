""" Number Guess game """
import random

def play_game():
    """Play a number guessing game where the user tries to guess a random number."""
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if user_guess == number_to_guess:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    play_game()
