from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # Homepage
    path('convert/', views.convert, name='convert'),  # Handles form POST
]
