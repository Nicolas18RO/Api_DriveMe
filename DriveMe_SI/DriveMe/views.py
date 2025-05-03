from .models import Driver, Customer, Route, Trip,TypeOfVehicle, Vehicle
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DriverSerializer, customerSerializaer,RoutesSerializer, TripsSerializer,TypeOfVehicleSerializer, VehicleSerializer
from rest_framework import generics, filters

# Create your views here.
# --------CRUD Driver--------
class ListCreateDriver(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RetrieveUpdateDeleteDriver(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

#----------CRUD Customer--------
class ListCreateCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializaer

class RetrieveUpdateDeleteCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializaer

#----------CRUD Routes--------
class ListCreateRoutes(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RoutesSerializer

class RetrieveUpdateDeleteRoutes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RoutesSerializer

#----------CRUD Trips--------
class ListCreateTrips(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripsSerializer

class RetrieveUpdateDeleteTrips(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripsSerializer


#----------CRUD TypeOfVehicle--------
class ListCreateTypeOfVehicle(generics.ListCreateAPIView):
    queryset = TypeOfVehicle.objects.all()
    serializer_class = TypeOfVehicleSerializer

class RetrieveUpdateDeleteTypeOfVehicle(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeOfVehicle.objects.all()
    serializer_class = TypeOfVehicleSerializer

#----------CRUD Vehicle--------
class ListCreateVehicle(generics.ListCreateAPIView):
    queryset =Vehicle.objects.all()
    sarializer_class =VehicleSerializer

class RetrieveUpdaterDeleteVehicle(generics.RetrieveUpdateDestroyAPIView):
    queryset =Vehicle.objects.all()
    serializer_class =VehicleSerializer 
    