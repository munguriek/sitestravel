from .models import Index
from datetime import datetime

def global_temp(request):
    try:
        temp = Index.objects.latest('last_updated')
    except:
        Index.objects.create(about_us="Sites Travel Ltd is a bespoke travel and tours management agency based in Uganda. We are a locally registered travel agency, certified by ATA, IATA and a member of Uganda Travel Bureau. We pride ourselves in more than 15 years of experience and expertise in the travel industry and our specialty is that point in life where you don’t know what to do next on your travel plans.", 
        about_image="", address="Kampala, Uganda", tel_1="+256 414 347 443", tel_2="+256 414 347 443", 
        email="reservations@sitestravel-ug.com", facebook="facebook link", twitter="twitter link", youtube="youtube link", 
        instagram="instagram link", last_updated=datetime.now())
        temp = Index.objects.latest('last_updated')
    return {
        "temp": temp
    }
        