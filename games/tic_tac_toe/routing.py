from django.urls import path

from . import consumers

# tic-tac-toe routing
# ws/tic-tac-toe/<room_id>/
websocket_urlpatterns = [
    path("ws/tic-tac-toe/<str:room_id>/", consumers.TicTacToeConsumer.as_asgi()),
]
