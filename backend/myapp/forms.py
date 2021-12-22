from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Accomadation, Booking, Car, Contact, Driver, Flight, Gallery, Trip, Category, Contact
import datetime
from django.forms import Form, ModelForm, DateField, widgets
from django_countries.widgets import CountrySelectWidget


class TripForm(forms.ModelForm):
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Trip destination'}))
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation on arrival')
    trip_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation on arrival')

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['destination'].label = "Trip destination"
        self.fields['image'].label = "Upload image(formats .png, .jpeg, jpg)"
        self.fields['slots'].placeholder = "Number of slots"
        self.fields['start'].label = "Trip starts on"
        self.fields['end'].label = "Trip ends on"
        self.fields['price'].placeholder = "Price(in Dollars)"
        self.fields['details'].placeholder = "Additional trip details"
        self.fields['details'].label = "Trip details"

    # def clean_date(self):
    #     date = self.cleaned_data['date']
    #     if self.start < datetime.date.today():
    #         raise forms.ValidationError("You should only book dates in the future!")
    #     return date

    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ('category', 'available', )   
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'}),
            'details': 	widgets.Textarea(attrs={'rows':4})
        } 


class FlightForm(forms.ModelForm):
    # start = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From '}))
    # destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'To'}))
    # price = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Price of flight'}))

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ('available', )   


class CarForm(forms.ModelForm):
    car = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter car '}))

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('available', )   
     

class GalleryForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Caption uploaded image'}))

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
    class Meta:
        model = Gallery
        fields = '__all__'
        exclude = ('hidden', )   


class BookingForm(forms.ModelForm):
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select')

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked',)
        

class TripBookingForm(forms.ModelForm):
    pickup = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter location to pick you up from'}))
    dropoff = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter a location to drop you at.'}))
    slots = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter number of trip participants'}))

    def __init__(self, *args, **kwargs):
        super(TripBookingForm, self).__init__(*args, **kwargs)
        self.fields['trip'].disabled = True 
        self.fields['service'].disabled = True 
        self.fields['slots'].label = "slots"
        self.fields['pickup'].label = "Pickup place"
        self.fields['dropoff'].label = "Drop-off place"
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('car', 'time_booked', 'car_hire', 'flight', 'flight_type', 'departure_date', 'adults', 'children', 
        'infants', 'driven_by', 'carhire_trip', 'booked_by', 'start', 'end',  )


class FlightBookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlightBookingForm, self).__init__(*args, **kwargs)
        self.fields['service'].disabled = True 
        self.fields['flight'].disabled = True 
        self.fields['start'].label = "Date of flight" 

    # def clean(self):
    #     start = self.cleaned_data.get('start')
    #     adults = self.cleaned_data.get('adults')
    #     children = self.cleaned_data.get('children')
    #     if start < datetime.date.today():
    #         raise forms.ValidationError("You should only book dates in the future!")
    #     if int(adults) + int(children) == 0:
    #         raise forms.ValidationError("Please fill in the number of people that will take the flight!")
    #     return start, adults, children 

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'car', 'end', 'trip', 'car_hire', 'pickup', 'dropoff', 'driven_by', 
        'carhire_trip', 'booked_by', 'slots', )
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'country': CountrySelectWidget()
        } 


class CarBookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarBookingForm, self).__init__(*args, **kwargs)
        self.fields['service'].disabled = True 
        self.fields['car'].disabled = True 
        self.fields['start'].label = "Date car hire starts"
        self.fields['end'].label = "Date car hire ends"
        self.fields['carhire_trip'].label = "Car hire within"

    # def clean(self):
    #     start = self.cleaned_data.get('start')
    #     end = self.cleaned_data.get('end')
    #     if start < datetime.date.today():
    #         raise forms.ValidationError("You should only book dates in the future!")
    #     elif end < start:
    #         raise forms.ValidationError("The end date has to be after the start date!")
    #     return start
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'flight', 'trip', 'flight_type', 'departure_date', 'pickup', 'dropoff',  'slots', 
        'adults', 'children', 'infants', 'booked_by',)
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'}),
        } 


class ContactForm(forms.ModelForm):  
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your full name '}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Phone number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your message'}))

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': 	widgets.Textarea(attrs={'rows':3})
        } 


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter category'}))
  
    class Meta:
        model = Category
        fields = '__all__'


class AccomodationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter name of accomodation'}))
    # budget = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter name of accomodation'}))

    class Meta:
        model = Accomadation
        fields = '__all__'
        exclude = ('available',)


