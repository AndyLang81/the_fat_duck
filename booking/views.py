from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from .forms import BookingForm
from django.http import HttpResponseRedirect

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'booking_success.html')
    else:
        form = BookingForm()
    
    return render(request, 'book_table.html', {'form': form})
