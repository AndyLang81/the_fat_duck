from django.db import models

# This model represents a single table booking in the restaurant
class Booking(models.Model):
    # Full name of the person booking the table
    name = models.CharField(max_length=100)

    # Email address of the person making the booking
    email = models.EmailField()

    # Number of guests included in the booking
    guests = models.PositiveIntegerField()  # Only allows 0 or positive integers

    # Date for the reservation (YYYY-MM-DD)
    date = models.DateField()

    # Time for the reservation (HH:MM[:ss[.uuuuuu]])
    time = models.TimeField()

    # String representation of a booking, used in admin panel and debug logs
    def __str__(self):
        return f"{self.name} — {self.date} at {self.time} for {self.guests} guest(s)"
