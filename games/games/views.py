from django.shortcuts import render

from ninja import NinjaAPI

app = NinjaAPI()


@app.get("/")
def index(request, name: str = "World"):
    context = {"name": name}
    return render(request, "index.html", context)
