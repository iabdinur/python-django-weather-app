from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/',views.about,name="about"),
    path('help/',views.help,name="help"),
]