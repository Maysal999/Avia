from urllib import request
from rest_framework import viewsets, generics, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter



from .models import  Plane, Aeroport, Ticket,Passenger, City
from .utils import TicketBasePagination
from .filters import TicketFilter
from .serializers import (
    PlaneSerializer,
    AeroportSerializer,
    TicketSeria,
    TicketSerializer,
    PassengerSerializer,
    CitySerializer,
    
  
)

class PlaneViewSets(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    pagination_class = TicketBasePagination



class AeroportViewSets(viewsets.ModelViewSet):
    queryset = Aeroport.objects.all()
    serializer_class = AeroportSerializer
    pagination_class = TicketBasePagination

class TicketViewSets(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = TicketBasePagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,OrderingFilter]
    filterset_class = TicketFilter
    search_fields = ['bag','plane','price','departure_date']
    ordering_fields = ['departure_date','arrived_date']
    ordering = ['departure_date']


class CityViewSets(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = TicketBasePagination

class PassengerViewSet(viewsets.ModelViewSet):
        queryset = Passenger.objects.all()
        serializer_class = PassengerSerializer

class TicketCreateAPIView(generics.CreateAPIView):
     queryset = Ticket
     serializer_class = TicketSeria
     


