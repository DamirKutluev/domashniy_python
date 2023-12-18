from django.urls import path
from .views import current_time



urlpatterns = [
    path('', current_time, name='current_time')
]