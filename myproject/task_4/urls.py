from django.urls import path
from .views import multiplication_table


urlpatterns = [
    path('', multiplication_table, name='multiplication_table')
]