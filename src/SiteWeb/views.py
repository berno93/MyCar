from datetime import datetime
from django.shortcuts import render

date = datetime.today()


def index(request):
    return render(request, "SiteWeb/index.html", context={"date": date})

