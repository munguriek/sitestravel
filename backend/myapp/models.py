from django.db import models
from django.db.models.fields.files import ImageField
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
User = get_user_model()


BUDGET = (
    ('budget', 'budget'),
    ('mid range', 'mid range'),
    ('up market', 'up market'),
)
class Accomadation(models.Model):
    """For both hotel and destination housing"""
    name = models.CharField(max_length=100)
    budget = models.CharField(max_length=100, choices=BUDGET)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


# PACKAGE_NAME = (
#     ('safari', 'safari'),
#     ('culture', 'culture'),
#     ('holiday', 'holiday'),
#     ('pilgramage', 'pilgramage'),
#     ('kampala special', 'kampala special'),
# )
class Category(models.Model):
    """Prepopulate into package, eg are safari, culture."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


CAR_CATEGORY = (
    ('executive', 'executive'),
    ('4x4', '4x4'),
    ('safari', 'safari'),
    ('vans', 'vans'),
    ('salon', 'salon'),
    ('buses', 'buses'),
    ('pickups', 'pickups'),
    ('trucks', 'trucks'),
)
class Car(models.Model):
    car = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cars")
    category = models.CharField(max_length=50, choices=CAR_CATEGORY)
    capacity = models.PositiveIntegerField(default=3)
    available = models.BooleanField(default=True)
    description = models.TextField()   

    class Meta:
        ordering = ['category']

    def __str__(self):
        return f"{self.car}"


PERMIT_CLASSES = (
    ('A', 'A - Motorcycles'),
    ('B', 'B - Motorcars and dual-purpose motor vehicles(Passenger vehicles up to 7 people and Goods vehicles up to 3.5 tonnes)'),
    ('CM', 'CM - Motorcars and dual-purpose motor vehicles'),
    ('CH', 'CH - Heavy goods vehicles'),
    ('DL', 'DL - Light omnibuses'),
    ('DM', 'DM - Medium omnibuses'),
    ('DH', 'DH - Heavy omnibuses'),
    ('E', 'E - Combination of vehicles'),
    ('F', 'F - Pedestrian-controlled vehicles'),
    ('G', 'G - Engineering plant vehicle'),
    ('H', 'G - Tractors'),
    ('I', 'G - Boats'),
)
class Driver(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    full_name = models.CharField(max_length=50)
    permit_class = models.CharField(max_length=100, default="DL")
    permit = models.FileField(upload_to="permits")
    photo = models.ImageField(upload_to="cars")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"


class Trip(models.Model):
    """Category of trip such as holiday, tour """
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    destination = models.CharField(max_length=100)
    image = models.ImageField(upload_to="trips")
    slots = models.PositiveIntegerField(default=0)
    start = models.DateField()
    end = models.DateField()
    price = models.PositiveIntegerField(default=0)
    arrival_accomodation = models.ForeignKey(Accomadation, on_delete=models.CASCADE, related_name="arrival_accom", null=True, blank=True)
    trip_accomodation = models.ForeignKey(Accomadation, on_delete=models.CASCADE, related_name="trip_accom", null=True, blank=True)
    details = models.TextField(null=True, blank=True) 
    available = models.BooleanField(default=True)

    def trip_duration(self):
        days = (self.end - self.start).days
        return days

    class Meta :
       ordering = ['destination']

    def __str__(self):
        return f"{self.destination}"


class Flight(models.Model):
    start = CountryField(blank_label='select country of flight origin')
    destination = CountryField(blank_label='select destination country')
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="flights")
    available = models.BooleanField(default=True)

    class Meta :
       ordering = ['-id']

    def __str__(self):
        return f"{self.start} - {self.destination}"


SERVICE = (
    ('trip', 'trip'),
    ('flight', 'flight'),
    ('car hire', 'car hire'),
)
DRIVER = (
    ('driver', 'our driver'),
    ('self', 'self'),
)
TRIP = (
    ('up country', 'up country'),
    ('town', 'town'),
)
class Booking(models.Model):
    service = models.CharField(max_length=50, choices=SERVICE, default="trip")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_booking", null=True) # For car hire
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    start = models.DateField(null=True) # For trips, car hire, flight
    end = models.DateField(null=True) # For trips, car hire   
    slots = models.PositiveIntegerField(default=0)
    adults = models.PositiveIntegerField(default=0) # For flight
    children = models.PositiveIntegerField(default=0) # For flight
    driven_by = models.CharField(max_length=40, choices=DRIVER, default='driver', null=True) # For car hire
    carhire_trip = models.CharField(max_length=100, choices=TRIP, default="up country") # For car hire
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_by')
    booked_on = models.DateTimeField(auto_now_add=True)

    def flight_slots(self):
        total = self.adults + self.children
        return total 

    def booking_duration(self):
        days = (self.end - self.start).days
        return days

    class Meta :
       ordering = ['-booked_on']

    def __str__(self):
        return f"{self.booked_by} booked {self.service}"


IMAGE_CATEGORY = (
    ('gallery', 'gallery'),
    ('partner', 'partner'),
)
class Gallery(models.Model):
    picture = models.ImageField(upload_to="gallery")
    category = models.CharField(max_length=50, choices=IMAGE_CATEGORY, default='gallery')
    caption = models.CharField(max_length=100, null=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.caption} - {self.category}"


class Contact(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=20, null=True)
    message = models.TextField()


