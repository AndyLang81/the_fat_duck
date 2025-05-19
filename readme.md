# The Fat Duck – Restaurant Booking System

A full-stack web application built with Django for a fictional medieval-style restaurant, The Fat Duck, located in Copenhagen. The project allows users to view the menu, learn about the restaurant, book tables, and access contact information, while giving the site owner full admin control over all bookings.

---

## Live Site

(Insert deployed Render URL here once deployed)

---

## Features

### External User Features

* View restaurant homepage, menu, contact, and about pages
* Make a booking by filling out a form with:

  * Name
  * Email
  * Phone number
  * Number of guests
  * Date
* Receive confirmation on successful booking
* Duplicate bookings prevented based on email and date

### Site Owner Features

* Log in to Django admin panel
* View, edit, and delete booking entries
* Admin dashboard secured with username and password

---

## Technologies Used

* Front-End: HTML5, CSS3, custom layout and styles
* Back-End: Python 3.13, Django 5.2.1
* Database: SQLite (default)
* Version Control: Git, GitHub
* Deployment: (Render to be added)

---

## Pages and URLs

| URL Path    | Description                          |
| ----------- | ------------------------------------ |
| `/`         | Home / Landing Page                  |
| `/menu/`    | Full food and drink menu             |
| `/book/`    | Table booking form                   |
| `/contact/` | Address, phone, and contact info     |
| `/about/`   | Info about owner, chef, and location |
| `/admin/`   | Django admin login (for staff)       |

---

## Design

* Old-timey tavern feel with emphasis on:

  * Hearty game and meat dishes
  * Sepia-toned illustrations of owner and chef
  * Serif font (Platypi)
  * Strong black & white contrast with warm accents
* Fully responsive
* Accessible layout and semantic HTML

---

## Functionality and Business Logic

* Booking model with unique email/date constraint
* CSRF token security for form submissions
* Validation for required fields (HTML + server side)
* Only authenticated users can access Django admin
* Static files served for custom images, stylesheets, and scripts

---

## Testing

* Manual testing performed on:

  * Form validation and error handling
  * Route rendering for all pages
  * Duplicate booking protection
  * Admin dashboard operations
* Static assets tested in browser
* Template rendering confirmed with Django routing
* Automated tests not implemented in this version

---

## Deployment

### Steps to deploy (Render):

1. Push code to GitHub repository
2. Log in to render.com
3. Create new Web Service:

   * Connect to GitHub
   * Select your repo
   * Build command: `pip install -r requirements.txt && python manage.py migrate`
   * Start command: `gunicorn the_fat_duck.wsgi:application`
   * Set environment variables (e.g. SECRET\_KEY, DEBUG=False)
4. Deploy and verify site loads properly

---

## Future Improvements

* Email notifications on booking
* Editable bookings via secure token
* Admin dashboard redesign
* Integration with a payment gateway
* Conversion of menu to database-driven structure

---

## Author

Anders Langhoff
Student Project – Code Institute Portfolio Project 4

---

## Credits

* Images generated with AI based on brief
* Fonts via Google Fonts
* Icons via FontAwesome CDN
* Initial layout and design by student, refined and adapted to Django

---

## License

This project is licensed for educational and portfolio purposes only.

---

## Status

Complete – all core features implemented, manually tested, and deployed. Minor polish and extensions may follow.
