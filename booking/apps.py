from django.apps import AppConfig  # Base class for app configurations

class BookingConfig(AppConfig):  # Configuration for the "booking" app
    default_auto_field = 'django.db.models.BigAutoField'  # Use BigAutoField for primary keys by default
    name = 'booking'  # App label used by Django to reference this app
