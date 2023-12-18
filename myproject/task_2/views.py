from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime




def current_time(request, *args, **kwargs):
    date = datetime.now()
    cur_time = date.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f'<h1>{cur_time}</h1>')
