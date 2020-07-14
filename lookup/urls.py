from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #as its the home page the first paranthesis is empty, otherwise say if it was about page then the '' would consist 'about' which would add up beside the url
    path('about', views.about, name="about"),

]