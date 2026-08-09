from collections import Counter
import random
import json

from game import WordleGame
from solver import Solver, convert_feedback

with open("wordles.json", "r") as f:
    answers = json.load(f)

with open("nonwordles.json", "r") as f:
    guesses = json.load(f)

NUM_ITERATIONS = len(answers)

turn_histogram = Counter()
wins = 0
total_turns = 0
losing_words = set()

for index, answer in enumerate(answers):
    game = WordleGame(answers, list(set(guesses + answers)), answer)
    solver = Solver()

    turns = 0

    while turns < 6:
        guess = solver.best_guess()
        turns += 1

        feedback = convert_feedback(game.make_guess(guess))

        if game.is_won():
            wins += 1
            total_turns += turns
            turn_histogram[turns] += 1
            break

        solver.update(guess, feedback)
    else:
        turn_histogram["Loss"] += 1
        losing_words.add(game.answer)
        # print("#####")
        # print(game.answer)
        # print("#####")
        # for guess in game.guesses:
        #     print(guess[0])
        
    

print(f"Games played : {NUM_ITERATIONS}")
print(f"Wins         : {wins}")
print(f"Win rate     : {100 * wins / NUM_ITERATIONS:.2f}%")

if wins:
    print(f"Average turns: {total_turns / wins:.3f}")

print("\nHistogram")

for turns in range(1, 7):
    count = turn_histogram[turns]
    pct = 100 * count / NUM_ITERATIONS
    bar = "#" * (count // 100)
    print(f"{turns}: {count:5} ({pct:5.2f}%) {bar}")

if turn_histogram["Loss"]:
    count = turn_histogram["Loss"]
    pct = 100 * count / NUM_ITERATIONS
    bar = "#" * (count // 100)
    print(f"L: {count:5} ({pct:5.2f}%) {bar}")

print("Losing words:")
print(losing_words)