from django.contrib import admin
from .models import Accomadation, Car, Flight, Gallery, Trip, Category, Booking, Driver, Contact

# Register your models here.
admin.site.register(Accomadation)
admin.site.register(Category)
admin.site.register(Trip)
admin.site.register(Flight)
admin.site.register(Car)
admin.site.register(Gallery)
admin.site.register(Booking)
admin.site.register(Driver)
admin.site.register(Contact)

