from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

class BookOrderTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_book_order(self):
        # Define the URL and the data for the request
        url = reverse('book-order')  # replace 'book_order' with the actual name of your view
        data = {'auth_code': 'AUTH_123456789', 'email': 'test@example.com', 'amount': '1000'}

        # Make a POST request to the view
        response = self.client.post(url, data)

        # Check the status code and the message in the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Payment successful')

# Create your tests here.
