from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('1/', views.page_1, name='page_1'),
    path('2/', views.page_2, name='page_2'),
    path('3/', views.page_3, name='page_3'),
]
