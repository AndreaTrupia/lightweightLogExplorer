from django.urls import path

from explorer import views

urlpatterns = [
    path('', views.home),
]
