from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from numpy import save
from .models import Data
import folium
from folium import plugins
from folium.plugins import MarkerCluster
# from kingcounty.data import mylist, results_df
from django.views.generic import ListView
import pandas as pd
# Create your views here.


def kincounty_project(request):
    # render(request,'/kingcounty/index.html')
    return render(request, 'kingcounty/base.html')


def home(request):
    x = pd.DataFrame()
    results_df = pd.read_csv('./kingcounty/summary.csv')
    x = results_df[["lat", "lot", "count_normal" ]]
    x['lat'].astype(float)
    x['lot'].astype(float)
    x['count_normal'].astype(float)
    my_array =x.to_numpy()
    mylist = my_array.tolist()
    
    df = results_df[["city", "count_ID"]]
    df["count_ID"].astype(int)
    df = df.sort_values(["count_ID", "city"], ascending=False)
    df.rename(columns = {'count_ID':'total crime'}, inplace = True)
    
    
    # this is for database rendering
    #data = Data.objects.all()
    #data_list = Data.objects.values_list("latitude", "longitude", "crime_count_normalized")
    #for data in data:
    #    print(data_list)
    m= folium.Map(location=[47.6062,-122.335167],zoom_start=9)
    
    # add marker one by one on the map
    for i in range(0,len(results_df)):
        folium.Circle(
        location=[results_df.iloc[i]['lat'], results_df.iloc[i]['lot']],
        popup=(results_df.iloc[i]['city'],results_df.iloc[i]['count_ID'].astype(int)),
        radius=float(results_df.iloc[i]['count_ID'])*10,
        color='crimson',
        fill=True,
        fill_color='crimson'
        ).add_to(m)
    
    #  gradient={0.1: 'blue', 0.3: 'lime', 0.5: 'yellow', 0.7: 'orange', 1: 'red'}
    """ plugins.HeatMap(mylist,radius=25,gradient={0.1: 'blue', 0.3: 'lime', 0.5: 'yellow', 0.7: 'orange', 1: 'red'},
                use_local_extrema=False).add_to(m) """
    m = m._repr_html_()
    context= {
        'm': m,"df":df.head(10).to_html(index=False,classes=["table-bordered",'table table-hover'], justify='left', col_space='50px')
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
    
    
