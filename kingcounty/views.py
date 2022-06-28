from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
import folium

# Create your views here.
def kincounty_project(request):
    #render(request,'/kingcounty/index.html')
    return render(request,'kingcounty/base.html')

def home(request):
    m= folium.Map(location=[47.5480,-121.9836],zoom_start=12)
    m = m._repr_html_()
    context= {
        'm': m,
    }
    return render(request, 'kingcounty/base.html',context)

def map(request):
    return render(request, 'kingcounty/map.html')
