from django.shortcuts import render, redirect
import random

navbar = [
    {"label": "Home", "url": "/"},
    {"label": "Tic-Tac-Toe", "url": "/tic-tac-toe"},
]


def index(request):
    context = {"navbarMenu": navbar}
    return render(request, "index.jinja", context)


def tic_tac_toe(request, room_id=None):
    # room id is a 6 random characters
    if room_id is None:
        room_id = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=6))
        # Redirect to the same view with the room_id
        return redirect("tic-tac-toe", room_id=room_id)

    # player id from the session
    player_id = request.session.get("player_id", None)

    if player_id is None:
        player_id = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=6))
        request.session["player_id"] = player_id

    context = {
        "navbarMenu": navbar,
        "room_id": room_id,
        "player_id": player_id,
    }

    return render(request, "tic-tac-toe.jinja", context)
