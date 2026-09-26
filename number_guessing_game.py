"""
Number Guessing Game
A beginner-friendly Python project demonstrating:
- Variables and Data Types (int, str, bool, list)
- Strings and formatting
- Conditionals (if, elif, else)
- Lists and list methods (append, in)
- Loops (while loop, for loop)
- Functions (def, parameters, return)
- Basic Module (random)
"""

import random


def show_welcome():
    """Display the game title and basic instructions."""
    print("=" * 45)
    print("      Welcome to the Number Guessing Game!   ")
    print("=" * 45)
    print("I have chosen a secret number between 1 and 100.")
    print("Try to guess it within the allowed attempts.\n")


def get_player_guess(previous_guesses):
    """
    Prompt the player for a guess, validate the input,
    and return the valid integer guess.
    """
    while True:
        user_input = input("Enter your guess (1-100): ").strip()

        # Check if the input contains only digits
        if not user_input.isdigit():
            print("Invalid input! Please enter a positive whole number.")
            continue

        # Convert string to integer
        guess = int(user_input)

        # Check if the number is within the allowed 1-100 range
        if guess < 1 or guess > 100:
            print("Out of range! Please enter a number from 1 to 100.")
            continue

        # Check if the number was already guessed
        if guess in previous_guesses:
            print(f"You already guessed {guess}! Try a different number.")
            continue

        # If valid and new, return the guess
        return guess


def play_round():
    """Play a single round of the guessing game."""
    # 1. Variables and basic module usage
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts_used = 0
    has_won = False  # Boolean flag

    # 2. List to store previous guesses
    previous_guesses = []

    print(f"You have {max_attempts} attempts. Good luck!\n")

    # 3. Main guessing loop (while loop)
    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"Attempts left: {remaining}")

        # Get a valid guess from the player
        guess = get_player_guess(previous_guesses)

        # Add the guess to our list of previous guesses
        previous_guesses.append(guess)
        attempts_used = attempts_used + 1

        # 4. Conditionals to check the guess
        if guess == secret_number:
            print(f"\n*** Congratulations! You found the secret number ({secret_number})! ***")
            print(f"It took you {attempts_used} attempt(s).")
            has_won = True
            break
        elif guess < secret_number:
            print("Too low! Try guessing higher.\n")
        else:
            print("Too high! Try guessing lower.\n")

        # 5. For loop: Display previous guesses to help the player
        print("Your guesses so far: ", end="")
        for num in previous_guesses:
            print(num, end=" ")
        print("\n" + "-" * 30)

    # If the player ran out of attempts without winning
    if not has_won:
        print("\nGame Over! You've used all your attempts.")
        print(f"The secret number was: {secret_number}")


def main():
    """Controls starting the game and replaying."""
    show_welcome()

    # Loop to allow playing again
    while True:
        play_round()

        # Ask if player wants another round
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if replay != "yes" and replay != "y":
            print("\nThanks for playing! Have a great day!")
            break

        print("\nStarting a new round...\n")


# Entry point of the program
if __name__ == "__main__":
    main()