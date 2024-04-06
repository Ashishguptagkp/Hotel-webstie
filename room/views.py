from django.shortcuts import render, redirect
from .models import Categary, Aminities, Booking, Rooms
from django.db.models import Q
# Create your views here.
def index(request):
    categary = Categary.objects.all()
    aminities = Aminities.objects.all()
    rooms = Rooms.objects.all()
    context = {'categary': categary, 'aminities':aminities, 'rooms':rooms}
    
    
    return render(request, 'index.html', context)


def check_room(request):
    categary_id = request.GET.get('categary')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    
    categary = Categary.objects.get(id = categary_id)
    already_booked_rooms = Booking.objects.filter(checkIn = check_in, checkOut = check_out, room__roomcategary_id = categary).values_list('room_id', flat=True)
    available_rooms = Rooms.objects.filter(roomcategary = categary, isbooked = False).exclude(id__in= already_booked_rooms)
    
    context = {'rooms': available_rooms}
    
    return render(request, 'available-room.html', context)


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


def apartment(request):
    return render(request, 'apartment.html')


def contact(request):
    return render(request, 'contact.html')