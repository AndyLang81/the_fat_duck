# booking/forms.py

import datetime
from django import forms
from .models import Booking

# Generate half-hour slots from 17:00 to 22:00
TIME_SLOTS = []
start = datetime.datetime(2000, 1, 1, 17, 0)
end   = datetime.datetime(2000, 1, 1, 22, 0)
delta = datetime.timedelta(minutes=30)

while start <= end:
    slot = start.time().strftime("%H:%M")
    TIME_SLOTS.append((slot, slot))
    start += delta

class BookingForm(forms.ModelForm):
    # Override time field to use a select dropdown of allowed slots
    time = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'guests', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            # time uses the select above
        }
