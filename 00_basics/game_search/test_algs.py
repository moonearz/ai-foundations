import pytest

from game_search.alpha_beta import alpha_beta
from game_search.minimax import minimax
from game_search.tic_tac_toe import Move, Player, State, TicTacToe

algorithms = [
    minimax,
    alpha_beta,
]


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_takes_immediate_win(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.EX,
            None,
            Player.OH,
            Player.OH,
            None,
            None,
            None,
            None,
        ),
        Player.EX,
    )

    move, value = algorithm(game, state)

    assert move == Move(2)
    assert value == 1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_blocks_immediate_loss(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.OH,
            Player.OH,
            None,
            Player.EX,
            None,
            None,
            None,
            None,
            None,
        ),
        Player.EX,
    )

    move, value = algorithm(game, state)

    assert move == Move(2)
    assert value == -1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_takes_winning_move_over_blocking(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.EX,
            None,
            Player.OH,
            None,
            None,
            Player.OH,
            None,
            None,
        ),
        Player.EX,
    )

    move, value = algorithm(game, state)

    assert move == Move(2)
    assert value == 1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_chooses_forced_loss(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.OH,
            Player.EX,
            Player.OH,
            Player.EX,
            None,
            None,
            None,
            None,
        ),
        Player.OH,
    )

    move, value = algorithm(game, state)

    assert move == Move(5)
    assert value == -1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_returns_draw_when_no_winner(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.OH,
            Player.EX,
            Player.EX,
            Player.OH,
            Player.OH,
            Player.OH,
            Player.EX,
            None,
        ),
        Player.EX,
    )

    move, value = algorithm(game, state)

    assert move == Move(8)
    assert value == 0


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_terminal_win(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.EX,
            Player.EX,
            Player.OH,
            Player.OH,
            None,
            None,
            None,
            None,
        ),
        Player.OH,
    )

    move, value = algorithm(game, state)

    assert move is None
    assert value == -1


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_terminal_draw(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.OH,
            Player.EX,
            Player.EX,
            Player.OH,
            Player.OH,
            Player.OH,
            Player.EX,
            Player.EX,
        ),
        Player.EX,
    )

    move, value = algorithm(game, state)

    assert move is None
    assert value == 0


@pytest.mark.parametrize("algorithm", algorithms)
def test_minimax_respects_maximizing_player(algorithm):
    game = TicTacToe()

    state = State(
        (
            Player.EX,
            Player.EX,
            None,
            Player.OH,
            Player.OH,
            None,
            None,
            None,
            None,
        ),
        Player.EX,
    )

    move, value = algorithm(game, state, Player.OH)

    assert move == Move(2)
    assert value == -1
