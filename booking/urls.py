from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Landing page view
    path('book/', views.book_table, name='book_table'), # Booking form and submission handler
]