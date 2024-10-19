from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Returns the index.html page
    return render(request, 'booking/index.html')

def booker(request):
    return HttpResponse("This is where you'll make bookings!")
