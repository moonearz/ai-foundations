from game import TileColor, WordleGame, get_feedback


def test_feedback_all_green():
    assert get_feedback("crane", "crane") == [
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
    ]


def test_feedback_all_gray():
    assert get_feedback("crane", "silly") == [
        TileColor.GRAY,
        TileColor.GRAY,
        TileColor.GRAY,
        TileColor.GRAY,
        TileColor.GRAY,
    ]


def test_feedback_yellow_letters():
    # c, r, and a exist in the answer but are in the wrong positions
    assert get_feedback("crane", "acrid") == [
        TileColor.YELLOW,
        TileColor.YELLOW,
        TileColor.YELLOW,
        TileColor.GRAY,
        TileColor.GRAY,
    ]


def test_feedback_duplicate_letters():
    # Answer contains only one 'a', so the extra 'a' in the guess
    # should not also be marked yellow.
    assert get_feedback("array", "cabin") == [
        TileColor.YELLOW,
        TileColor.GRAY,
        TileColor.GRAY,
        TileColor.GRAY,
        TileColor.GRAY,
    ]


def test_feedback_mixed_colors():
    assert get_feedback("crane", "crate") == [
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GRAY,
        TileColor.GREEN,
    ]


def test_game_valid_guess():
    game = WordleGame(answers=["crane"], possible_guesses=["crane", "slate"])

    assert game.is_valid_guess("crane")
    assert game.is_valid_guess("slate")
    assert not game.is_valid_guess("xxxxx")


def test_game_make_guess():
    game = WordleGame(answers=["crane"], possible_guesses=["crane"])

    feedback = game.make_guess("crane")

    assert feedback == [
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
        TileColor.GREEN,
    ]

    assert len(game.guesses) == 1
    assert game.guesses[0][0] == "crane"


def test_game_win_condition():
    game = WordleGame(answers=["crane"], possible_guesses=["crane"])

    assert not game.is_won()

    game.make_guess("crane")

    assert game.is_won()
    assert game.is_over()


def test_game_loss_condition():
    game = WordleGame(answers=["crane"], possible_guesses=["slate"])

    for _ in range(6):
        game.make_guess("slate")

    assert not game.is_won()
    assert game.is_over()
