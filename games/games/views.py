from django.shortcuts import render


navbar = [
    {"label": "Home", "url": "/"},
    {"label": "Tic-Tac-Toe", "url": "/tic-tac-toe"},
]


def index(request):
    context = {"navbarMenu": navbar}
    return render(request, "index.jinja", context)


def tic_tac_toe(request):
    context = {"navbarMenu": navbar}
    return render(request, "tic-tac-toe.jinja", context)
