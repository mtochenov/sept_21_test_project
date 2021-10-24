from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Pictures
from .forms import PicturesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView


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


class PicturesCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):  # Требуется аутентификация
    model = Pictures
    form_class = PicturesForm
    template_name = "gallery/add.html"
    success_url = reverse_lazy("gallery")  # Заменяет def get_absolute_url в models.py
    success_message = "Картина успешно добавлена"


class PicturesUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Pictures
    form_class = PicturesForm
    template_name = "gallery/update.html"
    success_url = reverse_lazy("gallery")
    success_message = "Картина успешно отредактирована"


class PicturesDeleteView(LoginRequiredMixin, DeleteView):
    model = Pictures
    success_url = '/gallery/'
    template_name = 'gallery/delete.html'
    context_object_name = "pictures"
