from django.urls import path
from .views import display_programmers_day


urlpatterns = [
    path('', display_programmers_day, name='display_programmers_day'),
]