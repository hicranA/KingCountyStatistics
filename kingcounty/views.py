from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Data
import folium
from folium import plugins



# Create your views here.
def kincounty_project(request):
    #render(request,'/kingcounty/index.html')
    return render(request,'kingcounty/base.html')

def home(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list("latitude", "longitude", "crime_count_normalized")
    for data in data:
        print(data_list)
    m= folium.Map(location=[47.5480,-121.9836],zoom_start=10)
    plugins.HeatMap(data_list).add_to(m)
    m = m._repr_html_()
    context= {
        'm': m,
    }
    return render(request, 'kingcounty/base.html',context)

def map(request):
    return render(request, 'kingcounty/map.html')
