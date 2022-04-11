from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from rest_framework import generics
from api import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.models import Index
from myapp.models import Trip, Flight, Car, Gallery, Booking, Driver, Contact
# from .serializers import (TripSerializer, FlightSerializer, CarSerializer, GallerySerializer, BookingSerializer)
from blog.models import Category, Post, Comment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from api.permissions import IsOwnerOrReadOnly, IsAdminUser

# HTML render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# TODO user detail with one positional arguement

class IndexList(generics.ListCreateAPIView):
    queryset = Index.objects.all()
    serializer_class = serializers.IndexSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class IndexDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Index.objects.all()
    serializer_class = serializers.IndexSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


# class WaitingList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'waiting.html'

#     def get(self, request):
#         queryset = User.objects.all()
#         return Response({'permission_level': queryset})


# TODO Toggle account activation, verify driver, admin rights

 
class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = serializers.TripSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = serializers.TripSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]



class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser] 




# Blog
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser] 


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser] 

