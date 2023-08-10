from datetime import datetime
from django.shortcuts import render

date = datetime.today()


def index(request):
    return render(request, "index.html", context={"prenom":"Berno", "date": date})

