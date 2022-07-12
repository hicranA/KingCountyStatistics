# in this file we will read one year of the crime data and we will add geo location to it 

########### LIBRARIES ###########
#  prefered using sodapy socrata instead of request library because this what king county used 
from sodapy import Socrata 
# dotenv libray to hide personal info
from dotenv import load_dotenv 
# os library to reach the variable
import os
# pandas to save as data frame
import pandas as pd
########################


######################## LOG IN TO KING COUNTY OPEN API ######################
# URL to king county api
url = "data.kingcounty.gov"
 
#load_dotenv() will load the variabled that we entered
load_dotenv()

# get this variable
USER_NAME =os.getenv("USER_NAME")
PASSWORD =os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")


# log in to the api using these variables 
client = Socrata(url, API_KEY,
                 username= USER_NAME,
                 password= PASSWORD)

######################## 


################################  LOAD CSV FILE ############
# load csv file and save as a df 
df = pd.read_csv('current_year.csv')
print(df.head())
##############################

########################## ADDING GEO LOCATION ###########

# We will save geolation to location array
location = []
# we will save how many times our search funtion ran
error_rate =[]

## we enter our criteria from our df and search to see if King county old api has this geolocation
## search function takes a string 
## the string has to match socrata api where clouse 
def searchFunc(final_string):
    results = client.get("rzfs-wyvy", where =final_string,limit=2000)
    # if we receive empty list from api our function returns to zero 
    if not results :
        print("result is empty")
        return 0
    # else our function returns to a geocode column
    else:
        results_df = pd.DataFrame.from_records(results)
        # some results does not have geolocation info, in this case return zero and search other altarnatives
        if 'geocoded_column' not in results_df:
            return 0
        else:
            # we will check our results too see if we have nan
            for i in range(len(results_df["geocoded_column"])):
                val = results_df["geocoded_column"][i]
                if type(val) != float:
                    return val
        return val

###

def tempfunc(final_string, count, x, y):
    print("temp on ")
    print("count is", count)
    print()
    my_val = searchFunc(final_string)
    print("myval is", my_val)
    if my_val !=0:
        print("sucess!")
        print(final_string)
        print(my_val)
        return (my_val, count)
    elif my_val == 0:
        print("empty")
        # count zero means it is the first time searching remove everything before the block
        if count == 0:
            print("count", count)
            print("modified", x)
            if type(x)== float:
                print("float")
                count = 4
                return tempfunc(final_string,count,x,y) 
            modified = x.split(" ",1)
            block_add = " '%{}%'".format(modified[1])
            print(block_add)
            city=  "'{}'".format(y)
            final_string = 'address_1 like' + " "+block_add + "and city == " + city
            print(final_string) 
            count = 1
            return tempfunc(final_string,count,x,y)
        elif count == 1:
            print("other")
            modified = x.split(" ",2)
            print("modified ",modified)
            block_add = " '%{}%'".format(modified[2])
            print(block_add)
            city=  "'{}'".format(y)
            final_string = 'address_1 like' + " "+block_add + "and city == " + city
            print(final_string)
            count = 2
            return tempfunc(final_string,count,x,y)
        elif count == 2:
            if len(x.strip().split(" ")) > 2:
                modified = x.split(" ",3)
                print("modified ",modified)
                block_add = " '%{}%'".format(modified[3])
                print(block_add)
                city=  "'{}'".format(y)
                final_string = 'address_1 like' + " "+block_add + "and city == " + city
                print(final_string)
            count = 3
            return tempfunc(final_string,count,x,y)
        elif count == 3:
            print("other")
            modified = x.split(" ",2)
            print("modified ",modified)
            block_add = " '%{}%'".format(modified[0])
            print(block_add)
            city=  "'{}'".format(y)
            final_string = 'address_1 like' + " "+block_add + "and city == " + city
            print(final_string)
            count = 4
            return tempfunc(final_string,count,x,y)
        elif count == 4:
            city=  "'{}'".format(y)
            final_string = "city == " + city
            print(final_string)
            count =5
            return tempfunc(final_string,count,x,y)
        else:
            count = 5
            print("last column")
            test= " "
            return (test,count)

########## for loop
count =0
for row in range(len(df)):
    print("#################")
    print("row is :", row)
    print()
    block_add = " '{}'".format(df["block_address"][row])
    city=  "'{}'".format(df["city"][row])
    final_string = 'address_1 ==' + " "+block_add + "and city == " + city
    print("final string is",final_string)
    #my_val = searchFunc(final_string)
    x= df["block_address"][row]
    y=df["city"][row]
    test, error_rate_num= tempfunc(final_string=final_string, count=count, x=x,y=y)
    print("result from search is ",test)
    location.insert(row, test)
    error_rate.insert(row, error_rate_num)
df["geocoded_column"]= location
df["error_rate"]= error_rate
print(df["block_address"])
print(df["geocoded_column"])

df.to_csv("current_geo.csv")
