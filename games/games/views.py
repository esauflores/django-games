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
    return render(request, "games/index.html", context)
