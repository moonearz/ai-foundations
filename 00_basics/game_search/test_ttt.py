import pytest

from game_search.tic_tac_toe import (
    Player,
    State,
    Move,
    TicTacToe,
    winner,
    board_full,
)


@pytest.fixture
def game():
    return TicTacToe()


def test_initial_state(game):
    state = game.initial_state()

    assert state.board == (None,) * 9
    assert state.player == Player.X


def test_current_player(game):
    state = State((None,) * 9, Player.O)

    assert game.current_player(state) == Player.O


def test_legal_moves_empty_board(game):
    state = game.initial_state()

    assert game.legal_moves(state) == [
        Move(0),
        Move(1),
        Move(2),
        Move(3),
        Move(4),
        Move(5),
        Move(6),
        Move(7),
        Move(8),
    ]


def test_legal_moves_partially_filled(game):
    state = State(
        (
            Player.X, None, Player.O,
            None, Player.X, None,
            Player.O, None, None,
        ),
        Player.X,
    )

    assert game.legal_moves(state) == [
        Move(1),
        Move(3),
        Move(5),
        Move(7),
        Move(8),
    ]


def test_make_move_places_player(game):
    state = game.initial_state()

    new_state = game.make_move(state, Move(4))

    assert new_state.board == (
        None, None, None,
        None, Player.X, None,
        None, None, None,
    )


def test_make_move_switches_player(game):
    state = game.initial_state()

    new_state = game.make_move(state, Move(4))

    assert new_state.player == Player.O


def test_make_move_does_not_modify_original_state(game):
    state = game.initial_state()

    game.make_move(state, Move(4))

    assert state.board == (None,) * 9
    assert state.player == Player.X


@pytest.mark.parametrize(
    "board, expected_winner",
    [
        # Rows
        (
            (
                Player.X, Player.X, Player.X,
                None, None, None,
                None, None, None,
            ),
            Player.X,
        ),
        (
            (
                None, None, None,
                Player.O, Player.O, Player.O,
                None, None, None,
            ),
            Player.O,
        ),

        # Columns
        (
            (
                Player.X, None, None,
                Player.X, None, None,
                Player.X, None, None,
            ),
            Player.X,
        ),
        (
            (
                None, Player.O, None,
                None, Player.O, None,
                None, Player.O, None,
            ),
            Player.O,
        ),

        # Diagonals
        (
            (
                Player.X, None, None,
                None, Player.X, None,
                None, None, Player.X,
            ),
            Player.X,
        ),
        (
            (
                None, None, Player.O,
                None, Player.O, None,
                Player.O, None, None,
            ),
            Player.O,
        ),
    ],
)
def test_winner(board, expected_winner):
    state = State(board, Player.X)

    assert winner(state) == expected_winner


def test_winner_no_winner():
    state = State(
        (
            Player.X, Player.O, None,
            None, Player.X, None,
            None, None, Player.O,
        ),
        Player.X,
    )

    assert winner(state) is None


def test_winner_empty_board():
    state = State((None,) * 9, Player.X)

    assert winner(state) is None


def test_board_full():
    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.O, Player.X, Player.O,
            Player.O, Player.X, Player.O,
        ),
        Player.X,
    )

    assert board_full(state)


def test_board_not_full():
    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.O, None, Player.O,
            Player.O, Player.X, Player.O,
        ),
        Player.X,
    )

    assert not board_full(state)


def test_terminal_when_x_wins(game):
    state = State(
        (
            Player.X, Player.X, Player.X,
            Player.O, Player.O, None,
            None, None, None,
        ),
        Player.O,
    )

    assert game.is_terminal(state)


def test_terminal_when_board_full(game):
    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.O, Player.X, Player.O,
            Player.O, Player.X, Player.O,
        ),
        Player.X,
    )

    assert game.is_terminal(state)


def test_not_terminal(game):
    state = State(
        (
            Player.X, Player.O, None,
            None, Player.X, None,
            None, None, Player.O,
        ),
        Player.X,
    )

    assert not game.is_terminal(state)


def test_evaluate_x_win_for_x(game):
    state = State(
        (
            Player.X, Player.X, Player.X,
            Player.O, Player.O, None,
            None, None, None,
        ),
        Player.O,
    )

    assert game.evaluate(state, Player.X) == 1


def test_evaluate_x_win_for_o(game):
    state = State(
        (
            Player.X, Player.X, Player.X,
            Player.O, Player.O, None,
            None, None, None,
        ),
        Player.O,
    )

    assert game.evaluate(state, Player.O) == -1


def test_evaluate_draw(game):
    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.O, Player.X, Player.O,
            Player.O, Player.X, Player.O,
        ),
        Player.X,
    )

    assert game.evaluate(state, Player.X) == 0