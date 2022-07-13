from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Data
import folium
from folium import plugins
#from kingcounty.final_model import df_1
#from django.views.generic import ListView


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

""" def bulkInsert(ListView):
    row_iter = df_1.iterrows()
    objs = [
        Data(
        city =row['city'],
        street_block = row['block_address'],
        crime_count = row['count'],
        crime_count_normalized = row['count_normal'],
        latitude = row['latitude'],
        longitude = row['longitude'],
        )
        for index, row in row_iter
    ]
    Data.objects.bulk_create(objs) """
