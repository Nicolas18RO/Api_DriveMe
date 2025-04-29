from django.urls import path 
from .views import (
    ListCreateDriver,
    RetrieveUpdateDeleteDriver,
    ListCreateCustomer,
    RetrieveUpdateDeleteCustomer,
    ListCreateRoutes,
    RetrieveUpdateDeleteRoutes,
    ListCreateTrips,
    RetrieveUpdateDeleteTrips,
    ListCreateEstimates,
    RetrieveUpdaterDeleteEstimates,
    ListrCreateVehicle,
    RetrieveUpdaterDeleteVehicle
)
urlpatterns = [
    path("driver/", ListCreateDriver.as_view(), name="list_create_driver"),
    path("driver/<int:pk>/", RetrieveUpdateDeleteDriver.as_view(), name="retrieve_update_delete_driver"),  
    path("customer/", ListCreateCustomer.as_view(), name="list_create_customer"),
    path("customer/<int:pk>/", RetrieveUpdateDeleteCustomer.as_view(), name="retrieve_update_delete_customer"),
    path("routes/", ListCreateRoutes.as_view(), name="list_create_routes"),
    path("routes/<int:pk>/", RetrieveUpdateDeleteRoutes.as_view(), name="retrieve_update_delete_routes"),
    path("trips/", ListCreateTrips.as_view(), name="list_create_trips"),
    path("trips/<int:pk>/", RetrieveUpdateDeleteTrips.as_view(), name="retrieve_update_delete_trips"),
    path("estimates/", ListCreateEstimates.as_view(), name="list_create_estimates"),
    path("estimates/<int:pk>/", RetrieveUpdaterDeleteEstimates.as_view(), name="retrieve_update_delete_estimates"),
    path("vehicle/", ListrCreateVehicle.as_view(), name="list_create_vehicle"),
    path("vehicle/<int:pk>/", RetrieveUpdaterDeleteVehicle.as_view(), name="retrieve_update_delete_vehicle" ),
]
 
 