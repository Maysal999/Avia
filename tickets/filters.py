import django_filters
from .models import Ticket


class TicketFilter(django_filters.FilterSet):
    bag = django_filters.CharFilter(field_name='bag__bag',lookup_expr='icontains')
    plane = django_filters.CharFilter(field_name='plane__plane',lookup_expr='icontains')
    aeroport = django_filters.CharFilter(field_name='aeroport__aeroport',lookup_expr='icontains')
    price = django_filters.CharFilter(field_name='ticket__price',lookup_expr='lt')
    reassingment = django_filters.CharFilter(field_name='ticket__reassingment',lookup_expr='lt')
    departure_date = django_filters.CharFilter(field_name='ticket__departure_date',lookup_expr='lt')
    city_flight = django_filters.CharFilter(field_name='ticket__city_flight',lookup_expr='icontains')
    city_arrived = django_filters.CharFilter(field_name='ticket__city_arrived',lookup_expr='icontains')

    class Meta:
        model = Ticket
        fields = ['bag','plane','aeroport','price','reassingment','departure_date','city_flight','city_arrived']
class PassengerFilter(django_filters.FilterSet):
    fio = django_filters.CharFilter(field_name='passenger__fio',lookup_expr='icontains')
    ticket = django_filters.CharFilter(field_name='ticket__flight_number',lookup_expr='icontains')
    class Meta:
        model = Ticket
        fields = ['fio','ticket']