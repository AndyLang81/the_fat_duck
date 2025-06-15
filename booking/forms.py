# booking/forms.py

import datetime  # for date and time manipulation
from django import forms  # Django form framework
from .models import Booking  # Booking model for the form

# Generate available half-hour time slots between 17:00 and 22:00
TIME_SLOTS = []
start = datetime.datetime(2000, 1, 1, 17, 0)  # dummy date with 17:00
end = datetime.datetime(2000, 1, 1, 22, 0)    # dummy date with 22:00
delta = datetime.timedelta(minutes=30)        # 30-minute interval

while start <= end:
    slot = start.time().strftime("%H:%M")     # format time as "HH:MM"
    TIME_SLOTS.append((slot, slot))           # choice tuple (value, display)
    start += delta                            

class BookingForm(forms.ModelForm):
    # Use a dropdown for the time field with our predefined slots
    time = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'guests', 'date', 'time']  # form fields
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # browser date picker
            # 'time' uses the custom ChoiceField above
        }
