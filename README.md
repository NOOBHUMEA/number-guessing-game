# 🎯 Number Guessing Game

Python-based game for beginners where the user attempts to guess a number that is randomly chosen by the computer within a range of 1 and 100.

This project illustrates some basic Python programming techniques including variables, data types, conditional statements, loops, functions, list, input validation, and the random module.

## ✨ Features

- 🎲 Random secret number between 1 and 100
- 🔢 Maximum of 7 attempts per round
- 💡 Hints when a guess is too high or too low
- 🚫 Prevents duplicate guesses
- ✅ Validates user input
- 📋 Displays previous guesses
- 🔄 Allows the player to play multiple rounds
- 💻 Runs completely from the command line

## 📚 Python Concepts

- Variables and data types
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
```

## ⚙️ Requirements

- Python 3
- A terminal
- No external libraries or packages are required.

## 🚀 Installation and Setup

### 1. Download the Project

Download the project files and extract the ZIP folder to your computer.

### 2. Check Python Installation

Open **Terminal** and run:

```bash
python --version
```
If your system uses `Python 3`, run:

```bash
python3 --version
```
Make sure Python 3 or newer.

## ▶️ Running the Game
```bash
python number_guessing_game.py
```
🎮 The game will start in the terminal.

## 📤Example output
```text
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
```

## 📦 Dependencies
- No external module are required.
- The project uses Python inbuild random module:

## 🧠 Concepts Used
- Variables
- Strings and Formatting
- Conditional Statements
- While Loops
- For Loops
- Lists
- Functions
- Random Module
- Input Validation
- Duplicate Input Handling
- Boolean
