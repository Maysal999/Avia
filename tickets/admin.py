from django.contrib import admin

from .models import (
    Plane,
   
    City,
    Aeroport,
    Ticket,
    Passenger

)


# Register your models here.
#бул жерде админ-панел болот



@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    '''Admin View for Bag'''

    list_display = ('plane',)
    

@admin.register(Aeroport)
class AeroportAdmin(admin.ModelAdmin):
    '''Admin View for Bag'''

    list_display = ('aeroport',)
    

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''Admin View for Bag'''

    list_display = ('city',)
    
# @admin.register(Cit1)
# class Cit1Admin(admin.ModelAdmin):
#     '''Admin View for Bag'''

#     list_display = ('city',)

@admin.register(Passenger)
class Buy_ticketAdmin(admin.ModelAdmin):
    '''Admin View for Bag'''

    list_display = ('fio','ticket')
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    '''Admin View for Bag'''

    list_display = ('flight_nomer','city_flight','city_arrived','bag','aeroport',
                    'plane','departure_date','arrived_date','price','reassingment')