from django.shortcuts import render


def home(request):
    data = {
        "title": "Home page"
    }
    return render(request, "main/home.html", data)


def page_1(request):
    data = {
        "title": "page 1"
    }
    return render(request, "main/page_1.html", data)


def page_2(request):
    data = {
        "title": "page 2"
    }
    return render(request, "main/page_2.html", data)


def page_3(request):
    data = {
        "title": "page 3"
    }
    return render(request, "main/page_3.html", data)
