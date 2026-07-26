import json
from solver import Solver

solver = Solver()

rankings_answers = solver.best_possible_answers(len(solver.possible_answers))
rankings_all = solver.best_guesses(len(solver.possible_guesses))

with open("initial_rankings_answers.json", "w") as f:
    json.dump(rankings_answers, f, indent = 2)

with open("initial_rankings_all.json", "w") as f:
    json.dump(rankings_all, f, indent = 2)