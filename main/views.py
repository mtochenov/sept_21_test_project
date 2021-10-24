from django.shortcuts import render


def home(request):
    data = {
        "title": "Home page"
    }
    return render(request, "main/home.html", data)
