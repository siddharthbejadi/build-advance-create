from django.urls import path
from . import views

urlpatterns = [
    # This makes your new view the homepage
    path('', views.home, name='home'),
]