import json

from channels.generic.websocket import WebsocketConsumer
from django.core.cache import cache

from .game import TicTacToe, Player
from asgiref.sync import async_to_sync


def player_from_json(json_data: dict) -> Player:
    return Player(json_data["name"], json_data["id"])


class TicTacToeConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "tic_tac_toe"

        # Increment the number of players in the game
        users_count = cache.get("tic_tac_toe_users_count", 0)
        cache.set("tic_tac_toe_users_count", users_count + 1)

        if users_count == 0:
            cache.set("tic_tac_toe", None)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json["type"] == "add_player":
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "add_player",
                    "player": text_data_json["player"],
                },
            )
        elif text_data_json["type"] == "make_move":
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "make_move",
                    "player": text_data_json["player"],
                    "row": text_data_json["row"],
                    "col": text_data_json["col"],
                },
            )
        else:
            pass

    def add_player(self, event):
        player = player_from_json(event["player"])

        game_state = cache.get("tic_tac_toe")
        if not game_state:
            game = TicTacToe()
        else:
            game = TicTacToe.from_dict(game_state)

        game.add_player(player)
        cache.set("tic_tac_toe", game.to_dict())

        self.send(text_data=json.dumps({"type": "game_state", "game": game.to_dict()}))

    def make_move(self, event):
        player = player_from_json(event["player"])
        row = event["row"]
        col = event["col"]

        game_state = cache.get("tic_tac_toe")
        if not game_state:
            game = TicTacToe()
        else:
            game = TicTacToe.from_dict(game_state)

        result = game.make_move(player, row, col)

        print(result)

        cache.set("tic_tac_toe", game.to_dict())

        self.send(text_data=json.dumps({"type": "game_state", "game": game.to_dict()}))

    def disconnect(self, close_code):
        # Decrement the number of players in the game
        users_count = cache.get("tic_tac_toe_users_count", 0)
        cache.set("tic_tac_toe_users_count", users_count - 1)

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
