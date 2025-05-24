from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Booking

# View to render the homepage
def home(request):
    return render(request, 'home.html')

# View to handle table bookings
def book_table(request):
    message = None  # To hold any error message shown to the user

    # Check if form was submitted
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Bind form to POST data

        if form.is_valid():
            # Extract cleaned/validated data from form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            guests = form.cleaned_data['guests']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Check if the same email already booked this time slot
            exists = Booking.objects.filter(date=date, time=time, email=email).exists()

            if exists:
                # Don't save duplicate booking — show message
                message = "You already have a booking at that time."
            else:
                # No conflict — save booking and redirect to success page
                form.save()
                return render(request, 'booking_success.html', {
                    "name": name,
                    "email": email,
                    "date": date,
                    "guests": guests,
                    "time": time
                })
    else:
        # If GET request, just show empty form
        form = BookingForm()

    # Render the booking form page with form and message (if any)
    return render(request, "book_table.html", {
        "form": form,
        "message": message
    })
