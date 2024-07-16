from django.db import models



class City(models.Model):
    city = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.city
    
class Bag(models.Model):
    bag = models.CharField(max_length=3)
    def __str__(self) -> str:
        return self.bag
    
class Aeroport(models.Model):
    aeroport = models.CharField(max_length=3)
    def __str__(self) -> str:
        return self.aeroport
    
class Plane(models.Model):
    plane = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.plane
    
class Ticket(models.Model):
    flight_nomer = models.CharField(max_length=60)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    bag = models.ForeignKey(Bag,on_delete=models.CASCADE)
    aeroport = models.ForeignKey(Aeroport,on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane,on_delete=models.CASCADE)
    flight_date = models.DateTimeField()
    arrived_date = models.DateTimeField()
    price = models.IntegerField()
    reassingment = models.IntegerField()


class Buy_ticket(models.Model):
    fio = models.CharField(max_length=70)
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    
    