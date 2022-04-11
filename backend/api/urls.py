from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('index', views.IndexList.as_view()),
    path('index/<int:pk>', views.IndexDetail.as_view()),    

    path('trips', views.TripList.as_view()),
    path('trips/<int:pk>', views.TripDetail.as_view()),

    path('flights', views.FlightList.as_view()),
    path('flights/<int:pk>', views.FlightDetail.as_view()),

    path('cars', views.CarList.as_view()),
    path('cars/<int:pk>', views.CarDetail.as_view()),

    path('gallery', views.GalleryList.as_view()),

    path('bookings', views.BookingList.as_view()),
    path('bookings/<int:pk>', views.BookingDetail.as_view()),

    path('drivers', views.DriverList.as_view()),
    path('drivers/<int:pk>', views.DriverDetail.as_view()),

    # Blog
    path('categories', views.CategoryList.as_view()),

    path('posts', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),

    path('comments', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
