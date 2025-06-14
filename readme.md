# The Fat Duck Tavern — Restaurant Booking System

Welcome to *The Fat Duck Tavern*, a full-stack web application designed to provide users with a seamless online table booking experience. This project was developed as part of a full-stack development course and showcases modern web development best practices, including responsive frontend design, a robust backend API, secure authentication, and cloud deployment.

---

## Project Overview

The Fat Duck Tavern app allows visitors to:

* View restaurant information, including the menu and contact details.
* Book tables online by submitting a reservation form with validation to prevent duplicate bookings.
* Receive a confirmation page summarizing their booking details.

Administrators can manage bookings securely through the Django admin interface.

The system is built with Django on the backend and standard HTML/CSS on the frontend, focusing on clean UX, accessibility, and maintainability.

---

## User Stories

### As a Visitor

* **As a visitor**, I want to view the restaurant’s home page so that I can learn about The Fat Duck Tavern.
* **As a visitor**, I want to browse the menu so that I can decide what I’d like to order.
* **As a visitor**, I want to fill out a reservation form with date, time, and guest count so that I can book a table.
* **As a visitor**, I want to receive a confirmation page after booking so that I know my reservation was successful.
* **As a visitor**, I want to access contact information so that I can reach out with questions or special requests.

### As an Administrator

* **As an administrator**, I want to log in to the admin panel so that I can manage reservations.
* **As an administrator**, I want to view all bookings in one place so that I can monitor restaurant occupancy.
* **As an administrator**, I want to edit or delete bookings so that I can handle cancellations or changes.
* **As an administrator**, I want to ensure no duplicate bookings for the same slot so that I avoid double-booking tables.

---

## Features

* **Responsive and Accessible UI:** Navigation adapts for mobile and desktop, forms include labels and client-side validation.
* **Booking Form Validation:** Prevents duplicate bookings by the same email for the same date/time slot.
* **Database-Backed:** All bookings are stored securely in a SQLite database with Django models.
* **Role-Based Authentication:** Django’s admin authentication controls access to administrative features.
* **Static File Management:** Uses WhiteNoise for efficient serving of CSS and images in production.
* **Cloud Deployment:** Hosted and deployed on Render.com, ensuring reliability and scalability.

---

## User Experience

The site was designed with simplicity and usability in mind. Key pages include:

* **Home:** Welcoming landing page introducing The Fat Duck Tavern.
* **Menu:** Displaying food and drink offerings.
* **Booking:** A clear form where users can reserve tables.
* **Confirmation:** A friendly confirmation page summarizing reservation details.
* **Contact & About:** Providing restaurant contact info and background.

The navigation menu remains consistent across pages, with a burger menu for smaller screens, ensuring smooth access anywhere.

---

## Installation and Running Locally

To run this project locally, ensure you have Python 3.10+ installed. Then:

```bash
git clone https://github.com/AndyLang81/the_fat_duck.git
cd the_fat_duck
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Create admin user
python manage.py collectstatic    # Prepare static files
python manage.py runserver
```

Visit XXXXX

---

## Deployment

The app is deployed on Render.com with environment variables set for secret keys and debug mode off for security. Static files are served efficiently using WhiteNoise. Deployment is configured to use Gunicorn as the production server.

---

## Screenshots
 coming

---

## Testing

Automated and manual tests have been conducted to ensure:

* Booking form validation works as expected.
* Navigation links function correctly.
* Access restrictions to admin pages are enforced.
* Static files load properly in production.

Further JavaScript testing for responsiveness and UX is planned.

---

## Technologies Used

* **Backend:** Python 3.13, Django 5.2
* **Frontend:** HTML5, CSS3, JavaScript (vanilla)
* **Database:** SQLite (development)
* **Deployment:** Render.com, Gunicorn, WhiteNoise

---

## Known Issues and Future Improvements

* Email notifications for bookings could be added.
* Additional user roles and permissions could enhance administration.
* More extensive frontend testing and improvements in accessibility.
* Transition to PostgreSQL for production database scalability.

---

## Author

This project was developed by Anders Lang as a portfolio piece demonstrating full-stack development skills, including project planning, database design, frontend and backend implementation, and deployment.

---

Thank you for reviewing The Fat Duck Tavern booking system. I welcome any feedback or questions.
