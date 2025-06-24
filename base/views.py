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
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break

    context = {'room': room}
    return render(request, 'base/room.html', context)

