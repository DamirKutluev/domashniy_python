from django.shortcuts import render
import datetime



def display_programmers_day(request, *args, **kwargs):
    current_year = datetime.datetime.now().year
    programmers_day = datetime.datetime(current_year, 9, 13) + datetime.timedelta(days=256)
    return render(request, 'task_5/index.html', {'programmers_day': programmers_day})