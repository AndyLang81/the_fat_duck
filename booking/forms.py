from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    # Override the time field to enforce 24-hour format
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type': 'time'},
            format='%H:%M'
        ),
        input_formats=['%H:%M']
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'guests', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            # 'time' is defined above to ensure 24-hour clock
        }
