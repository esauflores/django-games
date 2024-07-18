from django.shortcuts import render

from ninja import NinjaAPI

app = NinjaAPI()


navbar = [
    {"label": "Home", "url": "/"},
    {"label": "Games", "url": "/games"},
    {"label": "About", "url": "/about"},
]


@app.get("/")
def index(request, name: str = "World"):
    context = {"name": name, "navbarMenu": navbar}
    return render(request, "index.jinja", context)


@app.get("/tic-tac-toe")
def tic_tac_toe(request):
    context = {"title": "Tic Tac Toe", "navbarMenu": navbar}
    return render(request, "tic-tac-toe.jinja", context)
