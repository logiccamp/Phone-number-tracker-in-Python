from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def index (request) :
    context = {}
    status = 0
    context["status"] = status
    if(request.POST):
        number = request.POST["number"]
        context["number"] = number
        # valid_number = phonenumbers.parse(number, "NONE")
        # valid = phonenumbers.is_valid_number(valid_number)
        ch_number = phonenumbers.parse(number, 'CH')
        description = geocoder.description_for_number(ch_number, 'en')
        context["country"] = description
        ro_number = phonenumbers.parse(number, "RO")
        carriername = carrier.name_for_number(ro_number, 'en')
        context["carrier"] = carriername
        geodata_number = phonenumbers.parse(number, "GB")
        timezone_number = timezone.time_zones_for_geographical_number(geodata_number)
        context["timezone"] = timezone_number
        context['status'] = 1


    return render(request, "demoapp/index.html", context)
