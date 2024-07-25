from typing import List
import json


class Player:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    # Note: this is not a secure way to compare players
    def __eq__(self, other):
        return self.id == other.id

    # not equal
    def __ne__(self, other):
        return self.id != other.id

    def to_dict(self):
        return {"name": self.name, "id": self.id}

    def from_dict(data):
        return Player(data["name"], data["id"])


class TicTacToe:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.players: List[Player] = []
        self.winner = None
        self.game_start = False
        self.game_over = False
        self.turn = 0

    def add_player(self, player: Player):
        if len(self.players) == 2:
            return "Game is full"

        self.players.append(player)

        if len(self.players) == 2:
            self.game_start = True

    def make_move(self, player: Player, row: int, col: int) -> str | bool:

        if not self.game_start:
            return "Game hasn't started"

        if self.game_over:  # Game is over
            return "Game over"

        if row < 0 or row > 2 or col < 0 or col > 2:  # Invalid move
            return "Invalid move"

        if self.board[row][col] != "":  # Position already taken
            return "Invalid move"

        if player != self.players[self.turn % 2]:  # Not player's turn
            return "Not your turn"

        self.board[row][col] = player.id

        if self.check_winner(player):
            self.game_over = True
            self.winner = player.id
            return True

        if self.turn == 8:  # No more moves
            self.game_over = True
            return True

        self.turn += 1
        return True

    def check_winner(self, player: Player) -> bool:
        # Check rows
        for row in range(3):
            if (
                self.board[row][0]
                == self.board[row][1]
                == self.board[row][2]
                == player.id
            ):
                return True

        # Check columns
        for col in range(3):
            if (
                self.board[0][col]
                == self.board[1][col]
                == self.board[2][col]
                == player.id
            ):
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player.id:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player.id:
            return True

        return False

    def to_dict(self):
        return {
            "board": self.board,
            "players": [player.to_dict() for player in self.players],
            "winner": self.winner if self.winner else "",
            "game_start": self.game_start,
            "game_over": self.game_over,
            "turn": self.turn,
        }

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.players = []
        self.winner = None
        self.game_start = False
        self.game_over = False
        self.turn = 0

    def from_dict(data):
        game = TicTacToe()
        game.board = data["board"]
        game.players = [Player.from_dict(player) for player in data["players"]]
        game.winner = data["winner"]
        game.game_start = data["game_start"]
        game.game_over = data["game_over"]
        game.turn = data["turn"]
        return game
