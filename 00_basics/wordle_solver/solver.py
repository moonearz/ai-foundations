import json

with open("wordles.json", "r") as f:
    answers = json.load(f)

with open("nonwordles.json", "r") as f:
    guesses = json.load(f)