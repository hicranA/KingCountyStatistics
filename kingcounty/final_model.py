
import pandas as pd
import numpy as np
import folium
import folium 
from folium.plugins import HeatMap

################################  LOAD CSV FILE ############
# load csv file and save as a df 
df = pd.read_csv('/home/harnold/github/KingCountyStatistics//kingcounty/current_geo.csv')
print(df.head())
##############################

# count cases in the data frame 
final_map_model =   pd.DataFrame()
count_of_incidents = df["geocoded_column"].value_counts()
new_df = count_of_incidents.to_frame(name="count")
new_df.reset_index(inplace=True)
new_df.rename(columns={'index':'geocode'}, inplace = True)
print(new_df)
# how to split the gecode column
new_df["geocode"]= new_df["geocode"].astype(str)
new_df[['geocode', 'B', 'C']] = new_df['geocode'].str.split(':', 2, expand=True)
new_df['C'].str.replace('}',"")
new_df['C'] =new_df['C'].str.replace('}',"")
new_df['C'] =new_df['C'].str.replace(']',"")
new_df['C'] =new_df['C'].str.replace('[',"")
k = new_df['C'].str.split(',', 1, expand=True)
new_df['latitude']= k[0].astype(float)
new_df['longitude']= k[1].astype(float)
final_map_model['latitude']= new_df['latitude']
final_map_model['longitude']=new_df['longitude']
final_map_model['count']=new_df['count']
final_model_max = final_map_model["count"].max()
final_map_model["count_normal"]= final_map_model["count"]/final_model_max



############# create map ##################
x =   pd.DataFrame() 
x = final_map_model[["longitude","latitude","count_normal" ]]
x["longitude"]= x['longitude'].astype(float)
x["latitude"]= x['latitude'].astype(float)
x["count_normal"]= x['count_normal'].astype(float)
my_array =x.to_numpy()
mylist = my_array.tolist()

# that has any NaN values
indexList = [np.any(i) for i in np.isnan(mylist)]
# delete all the rows with any NaN value
arr = np.delete(mylist, indexList, axis=0)


""" # Get boolean index list of rows with True values for the rows
# that has any NaN values
indexList = [np.any(i) for i in np.isnan(mylist)]
# delete all the rows with any NaN value
arr = np.delete(mylist, indexList, axis=0)
print(arr)

mapObj = folium.Map([47.5480,-121.9836], zoom_control=100)
HeatMap(arr).add_to(mapObj)
mapObj.save("Map_test.html")  """
