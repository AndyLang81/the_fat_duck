from django.views.generic import TemplateView  # For rendering simple static templates
from django.contrib import admin              # Django admin site
from django.urls import path, include         # URL routing helpers

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface

    # Booking app routes
    path('', include('booking.urls')),  # Delegate root URL patterns to booking app

    # Static template pages
    path(
        "menu/",
        TemplateView.as_view(template_name="menu.html"),
        name="menu"
    ),  # Serve the menu page

    path(
        "contact/",
        TemplateView.as_view(template_name="contact.html"),
        name="contact"
    ),  # Serve the contact page

    path(
        "about/",
        TemplateView.as_view(template_name="about.html"),
        name="about"
    ),  # Serve the about page
]
