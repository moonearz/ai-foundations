from game import TileColor
from rich.console import Console
from rich.text import Text

console = Console()


def print_feedback(guess: str, feedback: list[TileColor]):
    row = Text()

    for letter, tile_color in zip(guess.upper(), feedback, strict=False):
        if tile_color == TileColor.GREEN:
            style = "black on green"
        elif tile_color == TileColor.YELLOW:
            style = "black on yellow"
        else:
            style = "white on grey30"

        row.append(f" {letter} ", style=style)

    console.print(row)


def create_keyboard():
    return {letter: None for letter in "abcdefghijklmnopqrstuvwxyz"}


def update_keyboard(keyboard, guess, feedback):
    for letter, tile_color in zip(guess, feedback, strict=False):
        current = keyboard[letter]

        if tile_color == TileColor.GREEN:
            keyboard[letter] = TileColor.GREEN
        elif tile_color == TileColor.YELLOW and current != TileColor.GREEN:
            keyboard[letter] = TileColor.YELLOW
        else:
            keyboard[letter] = TileColor.GRAY


def print_keyboard(keyboard):
    for row in ["qwertyuiop", "asdfghjkl", "zxcvbnm"]:
        text = Text()

        for letter in row:
            letter_color = keyboard[letter]

            if letter_color == TileColor.GREEN:
                style = "black on green"
            elif letter_color == TileColor.YELLOW:
                style = "black on yellow"
            elif letter_color == TileColor.GRAY:
                style = "black on grey30"
            else:
                style = "black on grey50"

            text.append(f" {letter.upper()} ", style=style)

        console.print(text)
