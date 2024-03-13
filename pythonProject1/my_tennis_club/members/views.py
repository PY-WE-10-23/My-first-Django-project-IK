from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

import datetime

def current_day_of_week(request):
    # Get the current date
    current_date = datetime.datetime.now()

    # Get the day of the week (0=Monday, 1=Tuesday, ..., 6=Sunday)
    day_of_week = current_date.weekday()

    # Convert the day of the week to a string representation
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_of_week = days_of_week[day_of_week]

    return render(request, 'day_of_week.html', {'current_day_of_week': current_day_of_week})