from django.urls import path
from . import views

urlpatterns = [
    path('', views.PicturesListView.as_view(), name='gallery'),
    path('add', views.gallery_add, name='gallery_add'),
    path('<int:pk>/delete', views.PicturesDeleteView.as_view(), name='gallery_delete'),
]
