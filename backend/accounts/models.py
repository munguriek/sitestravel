from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField

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
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile", null=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=20, null=True)
    permit_class = models.CharField(max_length=100, null=True)
    country = CountryField(blank_label='Select country citizenship')
    permit = models.FileField(upload_to="permits", null=True)
    is_driver = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.email


class Index(models.Model):
    # about_us = models.TextField(null=True)
    about_us = RichTextField()
    about_image = models.ImageField(upload_to="about")
    # breadcrumb_image = models.ImageField(upload_to="breadcrumb")
    address = models.CharField(max_length=50, null=True)
    tel_1 = models.CharField(max_length=20, null=True)
    tel_2 = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    youtube = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=50, null=True)
    tel_1 = models.CharField(max_length=20, null=True)
    tel_2 = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    youtube = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.last_updated}"