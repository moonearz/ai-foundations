from typing import Protocol, TypeVar

State = TypeVar("State")
Move = TypeVar("Move")
Player = TypeVar("Player")

class Game(Protocol[State, Move, Player]):
    def legal_moves(self, state: State) -> list[Move]:
        ...
    
    def make_move(self, state: State, move: Move) -> State:
        ...

    def is_terminal(self, state: State) -> bool:
        ...
    
    def evaluate(self, state: State, player: Player) -> float:
        ...

    def current_player(self, state: State) -> Player:
        ...

    def display(self, state: State) -> None:
        ...