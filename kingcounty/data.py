# in this file we will bring the current one year data from the king county data base 

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

######################### DONWLOAD 2022 DATA TO CSV ########################
# call api with a data range to and save as csv 
results = client.get("4kmt-kfqf",where= "updated_at between '2022-01-01T12:00:00' and '2022-12-01T14:00:00'")
# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df.to_csv('current_year.csv')
#####################
