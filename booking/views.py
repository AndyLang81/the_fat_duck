from django.shortcuts import render
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking
from datetime import time as dt_time, datetime

# Define opening hours (e.g., 17:00–22:00)
OPENING_TIME = dt_time(17, 0)
CLOSING_TIME = dt_time(22, 0)

# Maximum number of bookings allowed per slot (demo: 1)
MAX_PER_SLOT = 1

def parse_time(timestr):
    """
    Convert a 'HH:MM' string into a datetime.time object.
    """
    return datetime.strptime(timestr, "%H:%M").time()


# View to render the homepage and handle inline bookings
def home(request):
    message = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name      = form.cleaned_data['name']
            email     = form.cleaned_data['email']
            guests    = form.cleaned_data['guests']
            date      = form.cleaned_data['date']
            raw_time  = form.cleaned_data['time']
            slot_time = parse_time(raw_time)

            # Check opening hours
            if slot_time < OPENING_TIME or slot_time > CLOSING_TIME:
                message = (
                    f"Our opening hours are "
                    f"{OPENING_TIME.strftime('%H:%M')}–{CLOSING_TIME.strftime('%H:%M')}."
                )
            else:
                # Check slot availability
                count = Booking.objects.filter(date=date, time=slot_time).count()
                if count >= MAX_PER_SLOT:
                    message = "Sorry, that time slot is fully booked. Please choose another."
                else:
                    # Prevent duplicate bookings by same email
                    if Booking.objects.filter(date=date, time=slot_time, email=email).exists():
                        message = "You already have a booking at that time."
                    else:
                        # Save the booking (Django will accept the string or time object)
                        form.instance.time = slot_time
                        form.save()
                        return render(request, 'booking_success.html', {
                            "name": name,
                            "email": email,
                            "date": date,
                            "guests": guests,
                            "time": slot_time
                        })
    else:
        form = BookingForm()

    return render(request, 'home.html', {
        "form": form,
        "message": message
    })


# View to handle table bookings on its own page
def book_table(request):
    message = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name      = form.cleaned_data['name']
            email     = form.cleaned_data['email']
            guests    = form.cleaned_data['guests']
            date      = form.cleaned_data['date']
            raw_time  = form.cleaned_data['time']
            slot_time = parse_time(raw_time)

            # Check opening hours
            if slot_time < OPENING_TIME or slot_time > CLOSING_TIME:
                message = (
                    f"Our opening hours are "
                    f"{OPENING_TIME.strftime('%H:%M')}–{CLOSING_TIME.strftime('%H:%M')}."
                )
            else:
                # Check slot availability
                count = Booking.objects.filter(date=date, time=slot_time).count()
                if count >= MAX_PER_SLOT:
                    message = "Sorry, that time slot is fully booked. Please choose another."
                else:
                    # Prevent duplicate bookings by same email
                    if Booking.objects.filter(date=date, time=slot_time, email=email).exists():
                        message = "You already have a booking at that time."
                    else:
                        form.instance.time = slot_time
                        form.save()
                        return render(request, 'booking_success.html', {
                            "name": name,
                            "email": email,
                            "date": date,
                            "guests": guests,
                            "time": slot_time
                        })
    else:
        form = BookingForm()

    return render(request, "book_table.html", {
        "form": form,
        "message": message
    })


# Availability endpoint for AJAX checks
def availability(request):
    """
    Returns a JSON mapping of each time slot to the number of bookings
    already made on the provided date (YYYY-MM-DD).
    """
    date = request.GET.get('date')
    slots = {}

    # Prepare the list of possible slots from the BookingForm choices
    form = BookingForm()
    for choice, _ in form.fields['time'].choices:
        slots[choice] = 0

    if date:
        # Count existing bookings per slot
        counts = (
            Booking.objects
            .filter(date=date)
            .values_list('time')
            .order_by('time')
        )
        for slot_time in counts:
            time_str = slot_time[0].strftime("%H:%M")
            if time_str in slots:
                slots[time_str] += 1

    return JsonResponse(slots)
