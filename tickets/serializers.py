from rest_framework import serializers
from .models import Bag, Passenger, Plane, Aeroport, Ticket, City

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ['bag']
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
    flight_date = serializers.DateTimeField()
    arrived_date = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=9,decimal_places=2)
    reassingment = serializers.IntegerField()
    
    

class TicketSeria(serializers.ModelSerializer):
        class Meta:
             model = Ticket
             fields = '__all__'
        # fields = ['aeroport','plane','bag','city_flight','flight_nomer','city_arrived','flight_date','arrived_date','reassingment','price']
        
    


class PassengerSerializer(serializers.ModelSerializer):

        class Meta:
            model = Passenger
            fields = ['ticket','fio']

        # def create(self, validated_data):
        #     ticket_data = validated_data.pop('ticket')
        #     ticket = Ticket.objects.create(**ticket_data)
        #     passenger = Passenger.objects.create(ticket=ticket, **validated_data)
        #     return passenger

        # def update(self, instance, validated_data):
        #     ticket_data = validated_data.pop('ticket')
        #     ticket = instance.ticket

        #     instance.fio = validated_data.get('fio', instance.fio)
        #     instance.save()

        #     ticket.flight_nomer = ticket_data.get('flight_nomer', ticket.flight_nomer)
        #     ticket.flight_date = ticket_data.get('flight_date', ticket.flight_date)
        #     ticket.arrived_date = ticket_data.get('arrived_date', ticket.arrived_date)
        #     ticket.price = ticket_data.get('price', ticket.price)
        #     ticket.reassignment = ticket_data.get('reassignment', ticket.reassignment)
        #     ticket.city_flight = ticket_data.get('city_flight', ticket.city_flight)
        #     ticket.city_arrived = ticket_data.get('city_arrived', ticket.city_arrived)
        #     ticket.bag = ticket_data.get('bag', ticket.bag)
        #     ticket.aeroport = ticket_data.get('aeroport', ticket.aeroport)
        #     ticket.plane = ticket_data.get('plane', ticket.plane)
        #     ticket.save()

        #     return instance
    


# class Cit1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cit1
#         fields = '__all__'