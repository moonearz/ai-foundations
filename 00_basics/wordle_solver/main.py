import json
from game import WordleGame
from display import (
    print_feedback,
    print_keyboard,
    create_keyboard,
    update_keyboard,
)

with open("wordles.json", "r") as f:
    answers = json.load(f)

with open("nonwordles.json", "r") as f:
    possible_guesses = json.load(f)

game = WordleGame(answers, possible_guesses + answers)

keyboard = create_keyboard()

while not game.is_over():
    print_keyboard(keyboard)
    guess = input("Guess: ").strip().lower()
    if not game.is_valid_guess(guess):
        print("Invalid guess")
        continue

    feedback = game.make_guess(guess)
    print_feedback(guess, feedback)
    update_keyboard(keyboard, guess, feedback)

if game.is_won():
    print(f"You won! The word was {game.answer}.")
else:
    print(f"You lost. The word was {game.answer}.")