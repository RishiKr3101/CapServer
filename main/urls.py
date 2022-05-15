from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('response',views.response,name='response'),
]