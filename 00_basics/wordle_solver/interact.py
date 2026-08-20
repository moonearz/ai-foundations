from solver import Solver

solver = Solver()

while True:
    print()
    print(f"{solver.remaining_answers} possible answers remain")
    print()
    print("1. Show best entropy guesses")
    print("2. Show best possible answers")
    print("3. Show remaining answers")
    print("4. Enter feedback")
    print("5. Quit")

    choice = input("> ")

    if choice == "1":
        for word, entropy in solver.best_guesses(10):
            print(f"{word:10} {entropy:.3f}")

    elif choice == "2":
        for word, entropy in solver.best_possible_answers(10):
            print(f"{word:10} {entropy:.3f}")

    elif choice == "3":
        print(", ".join(solver.possible_answers))

    elif choice == "4":
        guess = input("Guess: ").lower()
        feedback = input("Feedback (g/y/x): ").lower()
        solver.update(guess, feedback)

    elif choice == "5":
        break
