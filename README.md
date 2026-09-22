# 🎯 Number Guessing Game

A beginner-friendly Python command-line game where the player tries to guess a randomly generated number between 1 and 100.

This project demonstrates fundamental Python programming concepts such as variables, data types, conditionals, loops, functions, lists, input validation, and the `random` module.

## ✨ Features

- 🎲 Random secret number between 1 and 100
- 🔢 Maximum of 7 attempts per round
- 💡 Hints when a guess is too high or too low
- 🚫 Prevents duplicate guesses
- ✅ Validates user input
- 📋 Displays previous guesses
- 🔄 Allows the player to play multiple rounds
- 💻 Runs completely from the command line

## 📚 Python Concepts Demonstrated

- Variables and data types (`int`, `str`, `bool`, `list`)
- String formatting and f-strings
- `if`, `elif`, and `else`
- `while` loops
- `for` loops
- Functions
- Function parameters and return values
- Lists and list methods
- User input and validation
- Built-in `random` module

## 📁 Project Structure

```text
number-guessing-game/
│
├── README.md
└── number_guessing_game.py
⚙️ Requirements
Python 3.8 or newer

A terminal or command prompt

No external libraries or packages are required.

🚀 Installation and Setup
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/number-guessing-game.git

2. Open the Project Directory
cd number-guessing-game

3. Check Python Installation
python --version

If your system uses python3:

python3 --version

Make sure Python 3.8 or newer is installed.

▶️ Running the Game
Windows
python number_guessing_game.py

macOS / Linux
python3 number_guessing_game.py

🎮 How to Play
The game generates a secret number between 1 and 100.

You have 7 attempts to guess the number.

Enter your guess when prompted.

The game tells you whether your guess is too high or too low.

Previously entered guesses cannot be used again.

Guess the number correctly to win.

If you use all 7 attempts, the secret number is revealed.

You can choose to play another round.

🛡️ Input Validation
The game checks that your input:

Is a positive whole number

Is between 1 and 100

Has not already been guessed

Example
Enter your guess (1-100): hello
Invalid input! Please enter a positive whole number.

Enter your guess (1-100): 150
Out of range! Please enter a number from 1 to 100.

Enter your guess (1-100): 50
You already guessed 50! Try a different number.

🖥️ Example Gameplay
=============================================
      Welcome to the Number Guessing Game!
=============================================
I have chosen a secret number between 1 and 100.
Try to guess it within the allowed attempts.

You have 7 attempts. Good luck!

Attempts left: 7
Enter your guess (1-100): 50
Too low! Try guessing higher.

Your guesses so far: 50
------------------------------

Attempts left: 6
Enter your guess (1-100): 75
Too high! Try guessing lower.

Your guesses so far: 50 75
------------------------------

Attempts left: 5
Enter your guess (1-100): 63

*** Congratulations! You found the secret number (63)! ***
It took you 3 attempt(s).

Would you like to play again? (yes/no): no

Thanks for playing! Have a great day!

🔧 Functions
show_welcome()
Displays the game title and basic instructions.

get_player_guess(previous_guesses)
Gets and validates the player's guess. It checks that the input is valid, within the range of 1 to 100, and has not already been guessed.

play_round()
Controls one complete round of the game, including generating the secret number, processing guesses, providing hints, and determining whether the player wins.

main()
Controls the overall program and allows the player to play multiple rounds.

📦 Dependencies
No third-party dependencies are required.

The project uses Python's built-in random module:

import random

