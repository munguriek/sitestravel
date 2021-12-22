from .models import Index
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

@receiver(post_save, sender=Index)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    print(sender)
    print(instance)
    print(created)
    if created:
        Index.objects.create(about_us="about sites safari", about_image="", address="Kampala, Uganda", tel_1="+256 414 347 443", 
            tel_2="+256 414 347 443", email="reservations@sitestravel-ug.com", facebook="facebook link",
            twitter="twitter link", youtube="youtube link", instagram="instagram link", last_updated=datetime.now())


