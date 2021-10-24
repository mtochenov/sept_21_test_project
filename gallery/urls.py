from django.urls import path
from . import views

urlpatterns = [
    path('', views.PicturesListView.as_view(), name='gallery'),
    path('<int:pk>/', views.PicturesDetailView.as_view(), name='detail'),
    path('add/', views.PicturesCreateView.as_view(), name='add'),
    path('<int:pk>/update/', views.PicturesUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PicturesDeleteView.as_view(), name='delete'),
]
