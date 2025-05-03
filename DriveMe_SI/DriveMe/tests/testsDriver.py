from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import status
from  import Driver, Customer, Route, Trip, TypeOfVehicle, Vehicle
from datetime import datetime, timedelta
 
class DriverTestCase(APITestCase):
    def setup(self):
        #crear la inatacia de la clase Driver
        self.driver =Driver.objects.create(
            document_driver="1898444",
            full_name_driver="Juan Perez",
            email_driver="juanPerez@gamil.com ",
            phone_driver="3001234567"
        )
    def test_list_drivers(self):
        response =self.client.get("/api/driver/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(status.HTTP_200_OK)


        