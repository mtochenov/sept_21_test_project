from django.shortcuts import render, redirect
from .models import Pictures
# from .forms import PicturesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


class PicturesListView(ListView):
    model = Pictures
    paginate_by = 2
    template_name = 'gallery/gallery.html'
    context_object_name = 'pictures'
    ordering = ['-id']
