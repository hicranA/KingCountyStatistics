from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from numpy import save
from .models import Data
import folium
from folium import plugins
#from kingcounty.data import mylist
from django.views.generic import ListView
import pandas as pd
# Create your views here.

def kincounty_project(request):
    #render(request,'/kingcounty/index.html')
    return render(request,'kingcounty/base.html')


def home(request):
    x =  pd.DataFrame()
    results_df = pd.read_csv('/home/harnold/github/KingCountyStatistics/kingcounty/summary.csv')
    x = results_df[["lat","lot","count_normal" ]]
    x["lat"]= x['lat'].astype(float)
    x["lot"]= x['lot'].astype(float)
    x["count_normal"]= x['count_normal'].astype(float)
    my_array =x.to_numpy()
    mylist = my_array.tolist()

    # this is for database rendering
    #data = Data.objects.all()
    #data_list = Data.objects.values_list("latitude", "longitude", "crime_count_normalized")
    #for data in data:
    #    print(data_list)
    m= folium.Map(location=[47.5480,-121.9836],zoom_start=9)
    plugins.HeatMap(mylist).add_to(m)
    m = m._repr_html_()
    context= {
        'm': m,
    }
    return render(request, 'kingcounty/base.html',context)

def map(request):
    return render(request, 'kingcounty/map.html')

""" def BulkInsert(ListView):
    row_iter = results_df.iterrows()  
    objs = [
        Data(
        city = row['city'],
        county = "United States",
        crime_count = row['count_ID'],
        crime_count_normalized = row['count_normal'],
        )
        for index, row in row_iter
    ]
    
    Data.objects.bulk_create(objs)  """
    
    
