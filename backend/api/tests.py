from rest_framework import status
from rest_framework.test import APITestCase
from api.models  import Car
import requests
from rest_framework.test import RequestsClient

class CarViewTest(APITestCase):

    @classmethod
    def setUp(cls) -> None:
        Car(name="CarTest", plate="ABC 123").save()
        return super().setUpTestData()
    
    def test_get_car_request(self):
        response = self.client.get("/api/cars/ABC 123")
        data = response.json()
        name = data['content']['car']['name']        
        self.assertEquals(name, "CarTest")
