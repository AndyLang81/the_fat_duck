from django import forms
from .models import Booking

# Form class tied to the Booking model, used to handle table reservations
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Use the Booking model as the base
        fields = ['name', 'email', 'guests', 'date', 'time']  # Fields to include in the form

        # Customize how date and time fields appear in the form (e.g., date/time pickers)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
