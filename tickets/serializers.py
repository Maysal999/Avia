from rest_framework import serializers

from .models import  Passenger, Plane, Aeroport, Ticket, City




class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['plane']

class AeroportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeroport
        fields = ['aeroport']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city']

class TicketSerializer(serializers.Serializer):
    flight_nomer = serializers.CharField(max_length=60)
    city_flight = serializers.CharField(max_length=60)
    city_arrived = serializers.CharField(max_length=60)
    bag = serializers.CharField(max_length=5)
    aeroport = serializers.CharField(max_length=60)
    plane = serializers.CharField(max_length=60)
    departure_date = serializers.DateTimeField()
    arrived_date = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=9,decimal_places=2)
    reassingment = serializers.IntegerField()
    
class TicketSeria(serializers.ModelSerializer):
        class Meta:
             model = Ticket
             fields = '__all__'
        
    


class PassengerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Passenger
            fields = '__all__'
