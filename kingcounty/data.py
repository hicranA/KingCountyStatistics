# in this file we will bring the current one year data from the king county data base 

########### LIBRARIES ###########
#  prefered using sodapy socrata instead of request library because this what king county used 
from sodapy import Socrata 
# dotenv libray to hide personal info

# os library to reach the variable
import os
# pandas to save as data frame
import pandas as pd
########################
from geopy.geocoders import Nominatim
######################## LOG IN TO KING COUNTY OPEN API ######################
# URL to king county api
url = "data.kingcounty.gov"
 

# log in to the api using these variables 
client = Socrata(url, API_KEY,
                 username= USER_NAME,
                 password= PASSWORD)


######################## 

query = """
select 
    city,
    count(ID)
where
    incident_datetime  between '2022-01-01T00:00:00' and '2022-12-31T23:00:00' and reporting_area != 'Out of Jurisdiction'
group by
    city
"""
results = client.get("4kmt-kfqf", query=query)
results_df = pd.DataFrame.from_records(results)
results_df['count_ID']= results_df["count_ID"].astype(float)
final_model_max = results_df["count_ID"].max()
results_df["count_normal"]= results_df["count_ID"]/final_model_max
print("size",len(results_df))


##########

geolocator = Nominatim(user_agent="Your_Name")
state= "Washington"
country ="United States"
lat=[]
lot =[]
results_df["city"].replace({"RAVESDALE": "RAVENSDALE"}, inplace=True)
for row in range(len(results_df)):
    print(row)
    city= results_df["city"].iloc[row]
    print(city)
    if city == "UNINCORPORATED KING COUNTY":
        print("yes")
        lat.insert(row, 47.4700)
        lot.insert(row, -121.8400)
    else:
        loc = geolocator.geocode(city+','+ ","+state+","+country)
        lat.insert(row, loc.latitude)
        lot.insert(row, loc.longitude)
  
results_df["lat"]= lat
results_df["lot"]= lot    
results_df.to_csv("summary.csv", index=False)
#results_df.to_csv("summary.csv", index=False)
#("latitude", "longitude", "crime_count_normalized")
""" x =   pd.DataFrame() 
x = results_df[["lat","lot","count_normal" ]]
x["lat"]= x['lat'].astype(float)
x["lot"]= x['lot'].astype(float)
x["count_normal"]= x['count_normal'].astype(float)
my_array =x.to_numpy()
mylist = my_array.tolist() """


""" 
######################### DONWLOAD 2022 DATA TO CSV ########################
# call api with a data range to and save as csv 
results = client.get_all("4kmt-kfqf",where= "incident_datetime between '2022-01-01T00:00:00' and '2022-12-31T23:00:00'")
# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(len(results_df))
#####################
 """
