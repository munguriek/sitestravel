from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http.response import HttpResponseRedirect
from .models import Flight, Gallery, Category, Trip, Car, Accomadation, Booking, Driver
from .forms import (TripForm, FlightForm, CarForm, GalleryForm, BookingForm, TripBookingForm, FlightBookingForm, 
CarBookingForm, CategoryForm, AccomodationForm, ContactForm) 
from blog.models import Post
from blog.forms import PostForm
from . import *
from django.contrib import messages
from datetime import datetime, timedelta, date
# import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def trip_list(request):
    trips = Trip.objects.filter(available=True)
    context = {
        'trips': trips,
    }
    return render(request, "trip-list.html", context)


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)

    booking_form = TripBookingForm(request.POST or None, request.FILES or None, 
        initial={"service": "trip", "trip": trip})
    if booking_form.is_valid():
        instance = booking_form.save(commit=False)
        instance.trip.slots = instance.trip.slots - instance.slots
        instance.trip.save()
        instance.start = instance.trip.start
        instance.end = instance.trip.end
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        instance.save()       
        messages.success(request, 'Trip booked successfully')
        return redirect('my_bookings')
    context = {
        'trip': trip,
        'booking_form': booking_form,
    }
    return render(request, "trip-detail.html", context)


def flight_list(request):
    flights = Flight.objects.filter(available=True)
    context = {"flights": flights}
    return render(request, "flight-list.html", context)


def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    booking_form = FlightBookingForm(request.POST or None, request.FILES or None, 
        initial={"service": "flight", "flight": flight })
    if booking_form.is_valid():
        instance = booking_form.save(commit=False)
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        if instance.start < date.today():
            messages.info(request, 'Please only book future dates')
            return redirect('flight_detail', flight.id)
        elif instance.adults + instance.children == 0:
            messages.info(request, 'Please enter number of people that will travel')
            return redirect('flight_detail', flight.id)
        else:
            instance.save()       
            messages.success(request, 'Flight booked successfully')
            return redirect('my_bookings')
    context = {
        'flight': flight,
        'booking_form': booking_form,
    }
    return render(request, "flight-detail.html", context)


def car_list(request):
    cars = Car.objects.filter(available=True)
    context = {"cars": cars}
    return render(request, "car-list.html", context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)

    booking_form = CarBookingForm(request.POST or None, request.FILES or None, 
        initial={"service": "car hire", "car": car })
    if booking_form.is_valid():
        instance = booking_form.save(commit=False)
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        if instance.start < date.today():
            messages.info(request, 'Please only book future dates')
            return redirect('car_detail', car.id)
        elif instance.start > instance.end:
            messages.info(request, 'Start date cannot be later than end date ')
            return redirect('car_detail', car.id)
        else:
            instance.save()       
            messages.success(request, 'Car hired successfully')
            return redirect('my_bookings')
    context = {
        'car': car,
        'booking_form': booking_form,
    }
    return render(request, "car-detail.html", context)


def gallery(request):
    pictures = Gallery.objects.filter(category="gallery", hidden=False)
    context = {
        "pictures": pictures,
    }
    return render(request, "gallery.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def pictures(request):
    pictures = Gallery.objects.filter(category="gallery", hidden=False)

    picture_form = GalleryForm(request.POST or None, request.FILES or None)
    if picture_form.is_valid():
        instance = picture_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Picture saved successfully')
        return redirect('pictures')
    context = {
        "pictures": pictures,
        "picture_form": picture_form,
    }
    return render(request, "admin/pictures.html", context)


def contacts(request):
    form = CarBookingForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Car Booked saved successfully')
        return redirect('contacts')

    contact_form = ContactForm(request.POST or None, request.FILES or None)
    if contact_form.is_valid():
        instance = contact_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Inquiry saved successfully')
        return redirect('contacts')
    context = {
        "contact_form": contact_form,
        "form": form,
    }
    return render(request, "contacts.html", context)





def step(request):
    context = {}
    return render(request, 'packages-group-detail.html', context)


def stepsave(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("step"))
    else:
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        telephone = request.POST.get('telephone')
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        start = request.POST.get('start')
        end = request.POST.get('end')
        slots = request.POST.get('slots')
        driven_by = request.POST.get('driven_by')
        carhire_trip = request.POST.get('carhire_trip')
        # if cpass != password:
        #     messages.error(request, "Error, passwords dont match") 
        #     return HttpResponseRedirect (reverse('multiformstepexample'))    

        try:
            multistepform = Booking(
                full_name=full_name, email=email, country=country, telephone=telephone, pickup=pickup, start=start, end=end,
                slots=slots, driven_by=driven_by, carhire_trip=carhire_trip)
            multistepform.save()
            messages.success(request, "Booking saved")
            return HttpResponseRedirect(reverse('step'))
        except:
            messages.error(request, "Error in saving booking data") 
            return HttpResponseRedirect(reverse('step'))







# Admin Dashboard
def main(request):
    if request.user.is_active:
        if request.user.is_staff or request.user.is_driver:
            # if request.user.is_staff
            trips = Trip.objects.all() 
            seen_trips = trips.filter(available=True).count()
            unseen_trips = trips.filter(available=False).count()

            accomodation = Accomadation.objects.all()
            accom_budget = accomodation.filter(budget="budget").count()
            accom_midrange = accomodation.filter(budget="mid range").count()
            accom_upmarket = accomodation.filter(budget="up market").count()

            car_hires = Car.objects.all()
            # carhire_town = car_hires.filter(trip="town service").count()
            # carhire_upcountry = car_hires.filter(trip="upcountry").count()

            bookings = Booking.objects.all()
            trips = bookings.filter(service="trip").count()
            flights = bookings.filter(service="flight").count()
            carhire = bookings.filter(service="car hire").count()

            # oneway_tickets = bookings.filter(flight_type="one way").count()
            # return_tickets = bookings.filter(flight_type="return").count()

            carhire_driver = bookings.filter(driven_by="driver").count()
            carhire_self = bookings.filter(driven_by="self").count()
            
            carhire_town = bookings.filter(carhire_trip="town service").count()
            carhire_upcountry = bookings.filter(carhire_trip="upcountry").count()

            blogs = Post.objects.all()
            draft = blogs.filter(status=0).count()
            published = blogs.filter(status=1).count()

            try:
                latest_booking = bookings.latest('time_booked')
            except:
                latest_booking = ""

            # tomorrow = datetime.date.today() + timedelta(days=1)
            # today = datetime.date.today()

            # for bk in bookings:
            #     bk_start = bk.start
            #     if bk_start == today:
            #         print("A booking starts today")
            #         bk_today = "Today"
            #     elif bk_start > today:
            #         print("A booking starts tomorrow")
            #         bk_tomoro = "tomoro"
        else:
            return redirect('my_bookings')
    else:
        return redirect('waiting')
        
    context = {
            "seen_trips": seen_trips,
            "unseen_trips": unseen_trips,
            "accom_budget" : accom_budget,
            "accom_mid_range": accom_midrange,
            "accom_up_market": accom_upmarket,
            "carhire_driver": carhire_driver,
            "carhire_self": carhire_self,
            "carhire_town": carhire_town,
            "carhire_upcountry": carhire_upcountry,
            "trips": trips,
            "flights": flights,
            "carhire": carhire,
            "draft": draft,
            "published": published, 
            # "bk_today": bk_today,
            # "bk_tomoro": bk_tomoro
            "latest_booking": latest_booking,
    }
    return render(request, "admin/main.html", context) 


def trips(request):
    if request.user.is_staff or request.user.is_driver:
        trips = Trip.objects.all()
    else:
        return redirect('waiting')

    trip_form = TripForm(request.POST or None, request.FILES or None)
    if trip_form.is_valid():
        instance = trip_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Package saved successfully')
        return redirect('trips')
    context = {
        'trips': trips,
        'trip_form': trip_form,
    }
    return render(request, "admin/trips.html", context)

def trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    update_trip = TripForm(request.POST or None, request.FILES or None, instance=trip)
    if update_trip.is_valid():
        instance = update_trip.save(commit=False)
        instance.save()                 
        messages.success(request, 'Trip updated successfully')
        return redirect('trip', trip.id)
    context = {
        'trip': trip,
        'update_trip': update_trip,
    }
    return render(request, "admin/trip.html", context)


def flights(request):
    if request.user.is_staff:
        flights = Flight.objects.all()
    else:
        return redirect('waiting')
    
    flight_form = FlightForm(request.POST or None, request.FILES or None)
    if flight_form.is_valid():
        instance = flight_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Flight saved successfully')
        return redirect('flights')
    context = {
        'flights': flights,
        'flight_form': flight_form,
    }
    return render(request, "admin/flights.html", context)

def flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    update_flight = FlightForm(request.POST or None, request.FILES or None, instance=flight)
    if update_flight.is_valid():
        instance = update_flight.save(commit=False)
        instance.save()                 
        messages.success(request, 'Flight updated successfully')
        return redirect('flight', flight.id)
    context = {
        'flight': flight,
        'update_flight': update_flight,
    }
    return render(request, "admin/flight.html", context)


def cars(request):
    if request.user.is_staff or request.user.is_driver:
        cars = Car.objects.all()
    else:
        return redirect('waiting')

    car_form = CarForm(request.POST or None, request.FILES or None)
    if car_form.is_valid():
        instance = car_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Car saved successfully')
        return redirect('cars')
    context = {
        'cars': cars,
        'car_form': car_form,
    }
    return render(request, "admin/cars.html", context)

def car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    update_car = CarForm(request.POST or None, request.FILES or None, instance=car)
    if update_car.is_valid():
        instance = update_car.save(commit=False)
        instance.save()                 
        messages.success(request, 'car updated successfully')
        return redirect('car', car.id)
    context = {
        'car': car,
        'update_car': update_car,
    }
    return render(request, "admin/car.html", context)

 
def bookings(request):
    if request.user.is_staff or request.user.is_driver:
        bookings = Booking.objects.all()
    else:
        return redirect('waiting')

    booking_form = BookingForm(request.POST or None, request.FILES or None)
    if booking_form.is_valid():
        instance = booking_form.save(commit=False)
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        instance.save()                 
        messages.success(request, 'Booking saved successfully')
        return redirect('bookings')
    context = {
        'bookings': bookings,
        'booking_form': booking_form,
    }
    return render(request, "admin/bookings.html", context)

def booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    update_booking = BookingForm(request.POST or None, request.FILES or None, instance=booking)
    if update_booking.is_valid():
        instance = update_booking.save(commit=False)
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        instance.save()                 
        messages.success(request, 'booking updated successfully')
        return redirect('booking', booking.id)
    context = {
        'booking': booking,
        'update_booking': update_booking,
    }
    return render(request, "admin/booking.html", context)






def profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    user_form = BookingForm(request.POST or None, request.FILES or None, instance=booking)
    if user_form.is_valid():
        instance = user_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'booking updated successfully')
        return redirect('booking', booking.id)
    context = {
        'drivers': profile,
    }
    return render(request, "admin/drivers.html", context)



def trip_availability(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if trip.available == True:
        trip.available = False
        trip.save()
        messages.info(request, 'Trip no longer available')
    else:
        trip.available = True
        trip.save() 
        messages.info(request, 'Trip now avaialable')
    return redirect('trips')

def flight_availability(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if flight.available == True:
        flight.available = False
        flight.save()
        messages.info(request, 'Flight no longer available')
    else:
        flight.available = True
        flight.save() 
        messages.info(request, 'Flight now avaialable')
    return redirect('flights')

def car_availability(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.available == True:
        car.available = False
        car.save()
        messages.info(request, 'Vehicle no longer available')
    else:
        car.available = True
        car.save() 
        messages.info(request, 'Vehicle now avaialable')
    return redirect('cars')




# multiforms
def step(request):
    context = {}
    return render(request, 'packages-group-detail.html', context)


def stepsave(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("step"))
    else:
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        telephone = request.POST.get('telephone')
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        start = request.POST.get('start')
        end = request.POST.get('end')
        slots = request.POST.get('slots')
        driven_by = request.POST.get('driven_by')
        carhire_trip = request.POST.get('carhire_trip')
        # if cpass != password:
        #     messages.error(request, "Error, passwords dont match") 
        #     return HttpResponseRedirect (reverse('multiformstepexample'))    

        try:
            multistepform = Booking(
                full_name=full_name, email=email, country=country, telephone=telephone, pickup=pickup, start=start, end=end,
                slots=slots, driven_by=driven_by, carhire_trip=carhire_trip)
            multistepform.save()
            messages.success(request, "Booking saved")
            return HttpResponseRedirect(reverse('step'))
        except:
            messages.error(request, "Error in saving booking data") 
            return HttpResponseRedirect(reverse('step'))
            


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def settings(request):
    accomodations = Accomadation.objects.all()
    high_end = accomodations.filter(budget="high end")
    mid_range = accomodations.filter(budget="mid range")
    budget = accomodations.filter(budget="budget")

    if accomodations.count() == 0:
        Accomadation.objects.create(name="nanjing hotel", budget="mid range", available=True )
    
    # categories =  Category.objects.all()

    # create views
    # category_form = CategoryForm(request.POST or None, request.FILES or None)

    # if category_form.is_valid():
    #     instance = category_form.save(commit=False)
    #     instance.save()                 
    #     messages.success(request, 'Trip category saved successfully')
    accomodation_form = AccomodationForm(request.POST or None, request.FILES or None)
    if accomodation_form.is_valid():
        instance = accomodation_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Accomodation saved successfully')
        return redirect('settings')

    context = {
        'accomodations': accomodations,
        'accomodation_form': accomodation_form,
    #     'categories': categories,
    #     'category_form': category_form,
        "high_end": high_end,
        "mid_range": mid_range,
        "budget": budget,
    }
    return render(request, "admin/settings.html", context)



@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def trip_categories(request):
    categories =  Category.objects.all()
    category_form = CategoryForm(request.POST or None, request.FILES or None)
    if category_form.is_valid():
        instance = category_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Trip category saved successfully')
        return redirect('trip_categories')
    context = {
        'categories': categories,
        'category_form': category_form,
    }
    return render(request, "admin/categories.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def accomodations(request):
    accomodations = Accomadation.objects.all()
    accomodation_form = AccomodationForm(request.POST or None, request.FILES or None)
    if accomodation_form.is_valid():
        instance = accomodation_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Accomodation saved successfully')
        return redirect('accomodations')
    context = {
        'accomodations': accomodations,
        'accomodation_form': accomodation_form,
    }
    return render(request, "admin/accomodations.html", context)