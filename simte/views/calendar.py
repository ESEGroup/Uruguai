from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def CalendarView(request):
    return render(request,'simte/calendar.html')
