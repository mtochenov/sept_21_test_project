from django.urls import path
from . import views


urlpatterns = [
    path('', views.PicturesListView.as_view(), name='gallery'),
    path('<int:pk>', views.PicturesDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.PicturesDeleteView.as_view(), name='delete'),
    path('add', views.gallery_add, name='add'),
]
