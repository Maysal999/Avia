from django.db import models

class Flight(models.Model):
    # This defines a Flight model which will be translated into a table in the database

    flight_number = models.CharField(max_length=10)
    # flight_number is a character field that stores the flight number, limited to 10 characters

    origin = models.CharField(max_length=100)
    # origin is a character field that stores the departure location of the flight, limited to 100 characters

    destination = models.CharField(max_length=100)
    # destination is a character field that stores the arrival location of the flight, limited to 100 characters

    departure_time = models.DateTimeField()
    # departure_time is a date-time field that stores the departure time of the flight

    arrival_time = models.DateTimeField()
    # arrival_time is a date-time field that stores the arrival time of the flight

    def __str__(self):
        return self.flight_number
    # The __str__ method returns the flight number when an instance of Flight is printed or converted to a string


class Passenger(models.Model):
    # This defines a Passenger model which will be translated into a table in the database

    first_name = models.CharField(max_length=50)
    # first_name is a character field that stores the passenger's first name, limited to 50 characters

    last_name = models.CharField(max_length=50)
    # last_name is a character field that stores the passenger's last name, limited to 50 characters

    email = models.EmailField()
    # email is a field that stores the passenger's email address

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # The __str__ method returns the passenger's full name when an instance of Passenger is printed or converted to a string


class Ticket(models.Model):
    # This defines a Ticket model which will be translated into a table in the database

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    # flight is a foreign key that references the Flight model, creating a relationship between Ticket and Flight
    # on_delete=models.CASCADE means if the referenced flight is deleted, all related tickets will also be deleted

    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    # passenger is a foreign key that references the Passenger model, creating a relationship between Ticket and Passenger
    # on_delete=models.CASCADE means if the referenced passenger is deleted, all related tickets will also be deleted

    seat_number = models.CharField(max_length=5)
    # seat_number is a character field that stores the seat number of the ticket, limited to 5 characters

    booking_date = models.DateTimeField(auto_now_add=True)
    # booking_date is a date-time field that stores the date and time the ticket was booked
    # auto_now_add=True means this field is automatically set to the current date and time when the ticket is created

    def __str__(self):
        return f"Ticket {self.id} for {self.passenger}"
    # The __str__ method returns a string representation of the ticket including its ID and associated passenger when an instance of Ticket is printed or converted to a string
