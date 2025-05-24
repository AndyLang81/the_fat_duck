from django.db import models

# This model represents a single table booking in the restaurant
class Booking(models.Model):
    # Full name of the person booking the table
    name = models.CharField(max_length=100)

    # Email address of the person making the booking
    email = models.EmailField()

    # Number of guests included in the booking
    guests = models.PositiveIntegerField()

    # Date for the reservation
    date = models.DateField()

    # Time for the reservation
    time = models.TimeField()

    # This defines how a booking will be displayed in the admin panel and elsewhere
    def __str__(self):
        return f"{self.name} — {self.date} at {self.time} for {self.guests} guest(s)"
