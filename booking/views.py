from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Booking

def home(request):
    return render(request, 'home.html')

def book_table(request):
    message = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            guests = form.cleaned_data['guests']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Check if the same email already booked this time slot
            exists = Booking.objects.filter(date=date, time=time, email=email).exists()

            if exists:
                message = "You already have a booking at that time."
            else:
                form.save()
                return render(request, 'booking_success.html', {
                    "name": name,
                    "email": email,
                    "date": date,
                    "guests": guests,
                    "time": time
                })
    else:
        form = BookingForm()

    return render(request, "book_table.html", {
        "form": form,
        "message": message
    })
