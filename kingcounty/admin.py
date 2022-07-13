from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display= ("city", "street_block","crime_count", "crime_count_normalized", "latitude", "longitude")

admin.site.register(Data, DataAdmin)
