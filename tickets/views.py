from rest_framework import viewsets, generics, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

import requests

from .models import Bag, Plane, Aeroport, Ticket,Passenger, City
from .utils import TicketBasePagination
from .filters import TicketFilter
from .serializers import (
    PlaneSerializer,
    BagSerializer,
    AeroportSerializer,
    TicketSerializer,
    PassengerSerializer,
    CitySerializer,
    TicketSeria
  
)

class PlaneViewSets(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    pagination_class = TicketBasePagination

class BagViewSets(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    pagination_class = TicketBasePagination

class AeroportViewSets(viewsets.ModelViewSet):
    queryset = Aeroport.objects.all()
    serializer_class = AeroportSerializer
    pagination_class = TicketBasePagination

class TicketViewSets(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = TicketBasePagination
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = ['bag','flight','plane','aeroport']
# class Buy_ticketViewSets(viewsets.ModelViewSet):
#     queryset = Passenger.objects.all()
#     serializer_class = 


class CityViewSets(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = TicketBasePagination
# class Cit1ViewSets(viewsets.ModelViewSet):
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer


class PassengerViewSet(viewsets.ModelViewSet):
        queryset = Passenger.objects.all()
        serializer_class = PassengerSerializer

class TicketFilterApiView(generics.ListAPIView):
     serializer_class = TicketSerializer
     queryset = Ticket.objects.all()
     filter_backends = [DjangoFilterBackend]
     filterset_class = TicketFilter
    #  search_fields = ['bag', 'plane','aeroport']
    #  def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Ticket.objects.all()
    #     bag = self.request.query_params.get('bag')
    #     bag = self.request.query_params.get('bag')
    #     bag = self.request.query_params.get('bag')
    #     if bag is not None:
    #         queryset = queryset.filter(ticket__bag=bag)
    #     return queryset