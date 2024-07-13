from rest_framework import viewsets, generics
from .models import Flight, Passenger, Ticket
from .serializers import FlightSerializer, PassengerSerializer, TicketSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class PassengerViewSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()