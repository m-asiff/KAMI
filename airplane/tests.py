from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Airplane

class AirplaneAPITestCase(APITestCase):

    def setUp(self):
        # Create sample airplanes for testing
        Airplane.objects.create(plane_id=1, passengers=100)
        Airplane.objects.create(plane_id=2, passengers=150)

    def test_get_airplanes(self):
        """
        Test retrieving a list of airplanes.
        """
        url = reverse('airplane-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_specific_airplane(self):
        """
        Test retrieving a single airplane by plane_id.
        """
        url = reverse('airplane-view', kwargs={'plane_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['plane_id'], 1)

    def test_create_airplane(self):
        """
        Test creating a new airplane.
        """
        url = reverse('airplane-view')
        data = {'plane_id': 3, 'passengers': 200}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 3)

    def test_update_airplane(self):
        """
        Test updating an existing airplane.
        """
        url = reverse('airplane-view', kwargs={'plane_id': 1})
        data = {'passengers': 120}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Airplane.objects.get(plane_id=1).passengers, 120)

    def test_delete_airplane(self):
        """
        Test deleting an airplane.
        """
        url = reverse('airplane-view', kwargs={'plane_id': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Airplane.objects.count(), 1)
