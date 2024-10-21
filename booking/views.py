from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    # Returns the index.html page
    return render(request, 'booking/index.html')

def booker(request):
    template = 'booking/booking.html'
    context = {
        'booker': booker,
    }
    return render(request, template, context)

def blog(request):
    template = 'booking/blog.html'
    context = {
        'blog': blog,
    }
    return render(request, template, context)

# A view to submit your preferred time after selecting your studio
def booking(request):
    # First I'll call a function to check which weekdays are available over the next 10 days

    # Next I'll make sure the user selects a date before continuing
    if request.method == 'POST':
        date = request.POST.get('booking_date')
        studio = request.POST.get('studio_id')
        if date == None:
            messages.success(request, "Please select a date!")
            return redirect('booking')

        request.session['booking_date'] = date
        request.session['studio_id'] = studio

        # Session data is stored and we're sent to the page where we'll choose our studio timeslot
        return redirect('booking_submit')

    template = 'booking.html'

    # In the context we'll return our valid weekdays from the function we called at the top of this one
    context = {}

    return render(request, template, context)

# A view for a user to confirm what time slot they want to book for
# This view will only allow users to select a timeslot that is not already booked
def booking_submit(request):
    user = request.username
    times = [
        "9am to 12pm",
        "12pm to 3pm",
        "3pm to 6pm"
    ]

    # Retrieve stored session data
    date = request.session.get('booking_date')
    studio = request.session.get('studio_id')

    # Call a function that only show users timeslots that haven't already been booked
    # This will iterate through the StudioBooking model to see if there is an entry in time for each time_slot
    # If there is, that timeslot won't be displayed

    # User is given a confirmation message of their studio, date and timeslot

    template = ''

    context = {}

    return render(request, template, context)

# A view for users to view their bookings

# A view for users to edit their bookings (will be similar to the booking view)

# Views for superusers to view and edit bookings