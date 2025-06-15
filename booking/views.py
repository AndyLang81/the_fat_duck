# booking/views.py

from django.shortcuts import render  # Render templates with context
from .forms import BookingForm     # Import the form for bookings
from .models import Booking        # Booking model for database operations

# View to render the homepage and handle inline bookings
def home(request):
    message = None  # Feedback message for the user

    if request.method == 'POST':
        form = BookingForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            # Extract cleaned data from the form
            name      = form.cleaned_data['name']
            email     = form.cleaned_data['email']
            guests    = form.cleaned_data['guests']
            date      = form.cleaned_data['date']
            slot_time = form.cleaned_data['time']

            # Check for existing booking with same email, date, and time
            exists = Booking.objects.filter(
                date=date, time=slot_time, email=email
            ).exists()
            if exists:
                message = "You already have a booking at that time."  # Duplicate booking
            else:
                form.save()  # Save new booking
                # Render success page with booking details
                return render(request, 'booking_success.html', {
                    "name": name,
                    "email": email,
                    "date": date,
                    "guests": guests,
                    "time": slot_time
                })
    else:
        form = BookingForm()  # Unbound form for GET requests

    # Render home template with form and any message
    return render(request, 'home.html', {
        "form": form,
        "message": message
    })


# View to handle table bookings on its own page
def book_table(request):
    message = None  # Feedback message for the user

    if request.method == 'POST':
        form = BookingForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            # Extract cleaned data from the form
            name      = form.cleaned_data['name']
            email     = form.cleaned_data['email']
            guests    = form.cleaned_data['guests']
            date      = form.cleaned_data['date']
            slot_time = form.cleaned_data['time']

            # Check for existing booking with same email, date, and time
            exists = Booking.objects.filter(
                date=date, time=slot_time, email=email
            ).exists()
            if exists:
                message = "You already have a booking at that time."  # Duplicate booking
            else:
                form.save()  # Save new booking
                # Render success page with booking details
                return render(request, 'booking_success.html', {
                    "name": name,
                    "email": email,
                    "date": date,
                    "guests": guests,
                    "time": slot_time
                })
    else:
        form = BookingForm()  # Unbound form for GET requests

    # Render book_table template with form and any message
    return render(request, "book_table.html", {
        "form": form,
        "message": message
    })
