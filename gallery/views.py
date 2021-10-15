from django.shortcuts import render, redirect
from .models import Pictures
from .forms import PicturesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView  # TODO: Задействовать все указанные классы


class PicturesListView(ListView):
    model = Pictures
    paginate_by = 1
    template_name = "gallery/gallery.html"
    context_object_name = "pictures"
    ordering = ["-id"]


class PicturesDetailView(DetailView):
    model = Pictures
    template_name = "gallery/detail.html"
    context_object_name = "pictures"


class PicturesDeleteView(DeleteView):
    model = Pictures
    success_url = '/gallery/'
    template_name = 'gallery/delete.html'
    context_object_name = "pictures"


def gallery_add(request):  # TODO: Заменить на CreateView
    error = ""
    if request.method == "POST":
        form = PicturesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gallery")
        else:
            error = "Форма была некорректно заполнена"

    form = PicturesForm()
    data = {
        "title": "Добавьте картину",
        "form": form,
        "error": error,
    }
    return render(request, "gallery/add.html", data)
