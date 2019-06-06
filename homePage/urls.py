from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('images', views.images, name='images'),
    path('upload', views.upload, name='upload')
]