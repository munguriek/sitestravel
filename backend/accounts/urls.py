from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_index', views.update_index, name='update_index'),
    path('waiting', views.waiting, name='waiting'),

    path('account_activation/<str:pk>', views.account_activation, name='account_activation'),
    path('verify_driver/<str:pk>', views.verify_driver, name='verify_driver'),
    path('admin_rights/<str:pk>', views.admin_rights, name='admin_rights'),
    
    path('users/', views.users, name='users'),
    path('user/<str:pk>', views.user, name='user'),
    path('profile', views.profile, name='profile'),
    path('my-bookings', views.my_bookings, name='my_bookings'),

    path('drivers', views.drivers, name='drivers'),

]
