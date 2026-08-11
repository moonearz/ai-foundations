from .game import Game, State, Move, Player
import math

def alpha_beta(game: Game, state: State, maximizing_player: Player | None = None, alpha: float = -math.inf, beta: float = math.inf) -> tuple[Move, float]:
    if maximizing_player is None:
        maximizing_player = game.current_player(state)
    if game.is_terminal(state):
        return None, game.evaluate(state, maximizing_player)
    
    legal_moves = game.legal_moves(state)
    is_maximizing = game.current_player(state) == maximizing_player
    best_move = legal_moves[0]
    if is_maximizing:
        best_value = -math.inf
    else:
        best_value = math.inf

    for move in legal_moves:
        outcome_state = game.make_move(state, move)
        _, value = alpha_beta(game, outcome_state, maximizing_player, alpha, beta)
        
        if is_maximizing:
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        else:
            if value < best_value:
                best_value = value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break

    return best_move, best_value

    
