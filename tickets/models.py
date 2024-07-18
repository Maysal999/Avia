from django.db import models

class City(models.Model):
    city = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.city

# 1

class Bag(models.Model):
    bag = models.CharField(max_length=3)
    def __str__(self) -> str:
        return self.bag
    
class Aeroport(models.Model):
    aeroport = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.aeroport
    
class Plane(models.Model):
    plane = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.plane



    
class Ticket(models.Model):
    flight_nomer = models.CharField(max_length=60)
    city_flight = models.ForeignKey(City,on_delete=models.CASCADE, related_name='departiva_city')
    city_arrived = models.ForeignKey(City,on_delete=models.CASCADE,related_name='arrived_sity')
    bag = models.ForeignKey(Bag,on_delete=models.CASCADE)
    aeroport = models.ForeignKey(Aeroport,on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane,on_delete=models.CASCADE)
    flight_date = models.DateTimeField()
    arrived_date = models.DateTimeField()
    price = models.DecimalField(max_digits=9,decimal_places=2)
    reassingment = models.IntegerField()
    def __str__(self) -> str:
        return self.flight_nomer

class Passenger(models.Model):
    fio = models.CharField(max_length=70)
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.ticket

    