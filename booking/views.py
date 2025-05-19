from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from .forms import BookingForm
from django.http import HttpResponseRedirect

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

            # Checks if date/time is already booked
            exists = Booking.objects.filter(date=date, time=time).exists()

            if exists:
                message = "Sorry, that time slot is already booked. Please choose another."
            else:
                form.save()
                return render(request, 'booking_success.html')
    else:
        form = BookingForm()

    return render(request, 'book_table.html', {'form': form, 'message': message})
