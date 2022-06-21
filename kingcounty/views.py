from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def kincounty_project(request):
    #render(request,'/kingcounty/index.html')
    return render(request,'kingcounty/index.html')
