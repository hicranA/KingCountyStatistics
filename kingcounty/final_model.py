
import pandas as pd
import numpy as np
import folium
import folium 
from folium.plugins import HeatMap

################################  LOAD CSV FILE ############
# load csv file and save as a df 
df = pd.read_csv('/home/harnold/github/KingCountyStatistics//kingcounty/current_geo.csv')
df_1= df.groupby(["city","block_address","geocoded_column"]).size().reset_index()
df_1.rename(columns = {0:'count'}, inplace = True)
print(df_1.loc[df_1["city"]=="ISSAQUAH"])
##############################


# how to split the gecode column
df_1["geocoded_column"]= df_1["geocoded_column"].astype(str)
df_1[['geocoded_column', 'B', 'C']] = df_1['geocoded_column'].str.split(':', 2, expand=True)
df_1['C'] =df_1['C'].str.replace('}',"")
df_1['C'] =df_1['C'].str.replace(']',"")
df_1['C'] =df_1['C'].str.replace('[',"")
k = df_1['C'].str.split(',', 1, expand=True)
df_1['latitude']= k[0].astype(float)
df_1['longitude']= k[1].astype(float)

columns = ['geocoded_column', 'B', 'C']
df_1.drop(columns, inplace=True, axis=1)

""" df_1[['geocoded_column', 'B', 'C']] = df_1['geocoded_column'].str.split(':', 2, expand=True)
df_1['C'].str.replace('}',"")
df_1['C'] =df_1['C'].str.replace('}',"")
df_1['C'] =df_1['C'].str.replace(']',"")
df_1['C'] =df_1['C'].str.replace('[',"")
k = df_1['C'].str.split(',', 1, expand=True)
df_1['latitude']= k[0].astype(float)
df_1['longitude']= k[1].astype(float)
final_model_max = df_1["count"].max()
df_1["count_normal"]= df_1["count"]/final_model_max """
print(df_1.columns)

""" 

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
arr = np.delete(mylist, indexList, axis=0) """


""" # Get boolean index list of rows with True values for the rows
# that has any NaN values
indexList = [np.any(i) for i in np.isnan(mylist)]
# delete all the rows with any NaN value
arr = np.delete(mylist, indexList, axis=0)
print(arr)

mapObj = folium.Map([47.5480,-121.9836], zoom_control=100)
HeatMap(arr).add_to(mapObj)
mapObj.save("Map_test.html")  """
