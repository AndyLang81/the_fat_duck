from django.test import TestCase
from django.urls import reverse

class SimpleViewTests(TestCase):
    def test_home_view_status_and_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')