from django.test import TestCase         # Django’s test framework base class
from django.urls import reverse         # Helper to build URLs by name

class SimpleViewTests(TestCase):
    def test_home_view_status_and_template(self):
        # Get the URL for the 'home' route
        url = reverse('home')
        # Issue a GET request to that URL
        response = self.client.get(url)
        # Verify we got an HTTP 200 OK response
        self.assertEqual(response.status_code, 200)
        # Verify the correct template was used to render the response
        self.assertTemplateUsed(response, 'home.html')
