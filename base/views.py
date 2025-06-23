from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 1 - learn python'},
    {'id': 2, 'name': 'Room 2 - Design with me'},
    {'id': 3, 'name': 'Room 3 - Frontend developers'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')

