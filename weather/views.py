from django.shortcuts import render
import json
import urllib.request
from datetime import datetime


# Create your views here.

def index(request):

    if request.method =='POST':
        city=request.POST["city"]
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6d2521639b4428d8765122465cda550c').read()
        json_data = json.loads(res)
        temp=str(json_data['main']['temp'])
        temp=round(float(temp)-273.15 , 2)
        
        data = {
            "city_name":str(json_data['name']),
            "cloudy":str(json_data['clouds']['all']),
            "wind":str(json_data['wind']['speed']),
            
            "temp": temp,
            "datetime": datetime.now(),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        data= {}
    return render(request, 'index.html', data)
