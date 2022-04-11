from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField  
# from accounts.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.models import Index
from myapp.models import Booking, Trip, Flight, Car, Gallery, Driver, Contact
from blog.models import Category, Post, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # post = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post_detail')
    class Meta:
        model = User
        fields = ('email', 'telephone', 'photo', 'full_name', 'permit_class', 'permit',  )
        # exclude = ('password',)


class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        # fields = '__all__'
        exclude = ('available', )


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        exclude = ('available', )        

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('available', )        


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ('hidden', )                


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'





# Blog
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    # url = HyperlinkedIdentityField(view_name="PostDetail", lookup_field="id")
    # owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Post
        # fields = ['title', 'slug', 'thumbnail', 'time', 'content', 'status', 'author', 'owner', 'url']
        exclude = ['status',]


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['author', 'post', 'content', 'content', 'status', 'time'] 
        exclude = ['status', ]




    

