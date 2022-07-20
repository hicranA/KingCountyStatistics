from kingcounty import views
from django.urls import include, path

urlpatterns = [
    path('kingcounty/', views.kincounty_project, name='project'),
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    #path('bulkInsert/', views.BulkInsert),# this if for bulk entry 
]
