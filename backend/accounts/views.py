from django.shortcuts import get_object_or_404, render, redirect
from .models import CustomUser, Index
from myapp.models import Accomadation, Trip, Gallery, Booking
from django.contrib import messages
from .models import Index
from .forms import CustomUserForm, IndexForm
from myapp.forms import IndexCarForm, IndexFlightForm, IndexTripForm, TripBookingForm, FlightBookingForm, CarBookingForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime, date

# Create your views here.
def error_404(request, exception):
        data = {}
        return render(request,'400.html', status=404)

def error_500(request):
        data = {}
        return render(request,'500.html', status=500) 

def waiting(request):
    return render(request,'waiting.html')


def index(request):
    pictures = Gallery.objects.all()
    partners = pictures.filter(category="partner")
    banners = pictures.filter(category="gallery")

    # trip
    trip_booking = IndexTripForm(request.POST or None, initial={"service": "trip"})
    if trip_booking.is_valid():
        instance = trip_booking.save(commit=False)
        instance.trip.slots = instance.trip.slots - instance.slots
        instance.trip.save()
        instance.start = instance.trip.start
        instance.end = instance.trip.end
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        instance.save()       
        messages.success(request, 'Trip booked successfully')
        return redirect('my_bookings')

    # Flight Booking form
    flight_booking = IndexFlightForm(request.POST or None, initial={"service": "flight"})
    if flight_booking.is_valid():
        instance = flight_booking.save(commit=False)
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        if instance.start < date.today():
            messages.info(request, 'Please only book future dates')
            return redirect('index')
        elif instance.adults + instance.children == 0:
            messages.info(request, 'Please enter number of people that will travel')
            return redirect('index')
        else:
            instance.save()       
            messages.success(request, 'Flight booked successfully')
            return redirect('my_bookings')

    # carbooking
    car_booking = IndexCarForm(request.POST or None, initial={"service": "car hire", })
    if car_booking.is_valid():
        instance = car_booking.save(commit=False)
        instance.booked_by = request.user
        instance.booked_on = datetime.now()
        if instance.start < date.today():
            messages.info(request, 'Please only book future dates')
            return redirect('index')
        elif instance.start > instance.end:
            messages.info(request, 'Start date cannot be later than end date ')
            return redirect('index')
        else:
            instance.save()       
            messages.success(request, 'Car hired successfully')
            return redirect('my_bookings')
    context = {
        "partners": partners,
        "banners": banners,
        'trip_booking': trip_booking,
        'flight_booking': flight_booking,
        'car_booking': car_booking,
    }
    return render(request, "index.html", context)


# @staff_member_required
@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def update_index(request):
    
    pg = Index.objects.latest('last_updated')
    page = get_object_or_404(Index, pk=pg.id)
    
    update_index = IndexForm(request.POST or None, request.FILES or None, instance=page)
    if update_index.is_valid():
        instance = update_index.save(commit=False)
        instance.save()                 
        messages.success(request, 'Index updated successfully')
        return redirect('index')

    context = {
        "page": page,
        "update_index": update_index,
    }
    return render(request, "admin/pages.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "admin/users.html", context)

def user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_form = CustomUserForm(request.POST or None, request.FILES or None, instance=user)
    if user_form.is_valid():
        instance = user_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'user updated successfully')
        return redirect('user', user.id)
    context = {
        "users": users,
        "update_user": user_form,
    }
    return render(request, "admin/user.html", context)

def profile(request):
    """User detail with only one positional arguement """
    user=request.user
    email=request.user.email
    profile = User.objects.filter(email=email)
    user_form = CustomUserForm(request.POST or None, request.FILES or None, instance=user)
    if user_form.is_valid():
        instance = user_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'user updated successfully')
        return redirect('user', user.id)
    context = {
        "users": users,
        "update_user": user_form,
    }
    return render(request, "admin/user.html", context)


def my_bookings(request):
    bookings = Booking.objects.filter(booked_by=request.user)
    context = {
        "bookings": bookings,
    }
    return render(request, "my-bookings.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def drivers(request):
    drivers = User.objects.filter(is_driver=True)
    print(drivers)
    context = {
        'drivers': drivers,
    }
    return render(request, "admin/drivers.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def account_activation(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active == True:
        user.is_active = False
        user.save()
        messages.info(request, 'Account suspended')
    else:
        user.is_active = True
        user.save() 
        messages.info(request, 'Account now active')
    return redirect('users')


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def verify_driver(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_driver == True:
        user.is_driver = False
        user.save()
        messages.info(request, 'Driver rights of user removed')
    else:
        user.is_driver = True
        user.save() 
        messages.info(request, 'Driver rights of user granted')
    return redirect('users')


@user_passes_test(lambda u: u.is_staff, login_url='waiting') 
def admin_rights(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_staff == True:
        user.is_staff = False
        user.save()
        messages.info(request, 'Admin rights of user removed')
    else:
        user.is_staff = True
        user.save() 
        messages.info(request, 'Admin rights of user granted')
    return redirect('users')