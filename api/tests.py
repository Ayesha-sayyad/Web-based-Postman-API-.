from django.test import TestCase

# Create your tests here.
# api/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CachedSum
import hashlib
import json

class calculate_sum(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/sum/'

    def test_sum_positive_case(self):
        data = {"numbers": [1, 2, 3, 4]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sum'], 10)
        self.assertFalse(response.data['cached'])

    def test_sum_cached_case(self):
        data = {"numbers": [5, 5]}
        # First request (not cached)
        first_response = self.client.post(self.url, data, format='json')
        self.assertEqual(first_response.status_code, status.HTTP_200_OK)
        self.assertFalse(first_response.data['cached'])

        # Second request (should be cached)
        second_response = self.client.post(self.url, data, format='json')
        self.assertEqual(second_response.status_code, status.HTTP_200_OK)
        self.assertTrue(second_response.data['cached'])

    def test_invalid_input_not_a_list(self):
        data = {"numbers": "123"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("numbers", response.data['error'])

    def test_missing_numbers_key(self):
        data = {"wrongkey": [1, 2, 3]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Missing", response.data['error'])

    def test_non_integer_elements(self):
        data = {"numbers": [1, "two", 3]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("integers", response.data['error'])
