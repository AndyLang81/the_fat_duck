from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    path("menu/", TemplateView.as_view(template_name="menu.html"), name="menu"),
]
