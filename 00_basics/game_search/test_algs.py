import pytest

from game_search.tic_tac_toe import Player, State, Move, TicTacToe
from game_search.minimax import minimax
from game_search.alpha_beta import alpha_beta


algorithms = [
    minimax,
    alpha_beta,
]


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_takes_immediate_win(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.X, None,
            Player.O, Player.O, None,
            None, None, None,
        ),
        Player.X,
    )

    move, value = algorithm(game, state)

    assert move == Move(2)
    assert value == 1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_blocks_immediate_loss(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.O, Player.O, None,
            Player.X, None, None,
            None, None, None,
        ),
        Player.X,
    )

    move, value = algorithm(game, state)

    assert move == Move(2)
    assert value == -1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_takes_winning_move_over_blocking(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.X, None,
            Player.O, None, None,
            Player.O, None, None,
        ),
        Player.X,
    )

    move, value = algorithm(game, state)

    assert move == Move(2)
    assert value == 1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_chooses_forced_loss(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.O, Player.X, None,
            None, None, None,
        ),
        Player.O,
    )

    move, value = algorithm(game, state)

    assert move == Move(5)
    assert value == -1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_returns_draw_when_no_winner(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.X, Player.O, Player.O,
            Player.O, Player.X, None,
        ),
        Player.X,
    )

    move, value = algorithm(game, state)

    assert move == Move(8)
    assert value == 0


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_terminal_win(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.X, Player.X,
            Player.O, Player.O, None,
            None, None, None,
        ),
        Player.O,
    )

    move, value = algorithm(game, state)

    assert move is None
    assert value == -1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_terminal_draw(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.O, Player.X,
            Player.X, Player.O, Player.O,
            Player.O, Player.X, Player.X,
        ),
        Player.X,
    )

    move, value = algorithm(game, state)

    assert move is None
    assert value == 0


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_respects_maximizing_player(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.X, Player.X, None,
            Player.O, Player.O, None,
            None, None, None,
        ),
        Player.X,
    )

    move, value = algorithm(game, state, Player.O)

    assert move == Move(2)
    assert value == -1