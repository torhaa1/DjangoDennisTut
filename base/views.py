from django.shortcuts import render
from django.http import HttpResponse

from .models import Room

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Room 1 - learn python'},
#     {'id': 2, 'name': 'Room 2 - Design with me'},
#     {'id': 3, 'name': 'Room 3 - Frontend developers'}
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

