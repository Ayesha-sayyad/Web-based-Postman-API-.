from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class SumAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/sum/'

    def test_valid_sum(self):
        data = {"numbers": [1, 2, 3]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sum'], 6)
        self.assertIn('cached', response.data)

    def test_cache_retrieval(self):
        data = {"numbers": [4, 5]}
        # First request - calculate and store
        self.client.post(self.url, data, format='json')
        # Second request - should be cached
        response = self.client.post(self.url, data, format='json')
        self.assertTrue(response.data['cached'])

    def test_empty_list(self):
        data = {"numbers": []}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sum'], 0)

    def test_invalid_string_input(self):
        data = {"numbers": "123"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_integer_in_list(self):
        data = {"numbers": [1, "a", 3]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_numbers_key(self):
        data = {}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
