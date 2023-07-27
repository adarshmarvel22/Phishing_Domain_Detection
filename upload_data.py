from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb+srv://adarsh:HelloWorld123@ineuron.sboiusu.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create db name and collection name
DATABASE_NAME="ineuron"
COLLECTION_NAME="phishingdomain"

# read data as df
df=pd.read_csv(r"C:\Users\adars\Downloads\Phishing_Domain_Detection\notebooks\data\dataset_full.csv")

# convert data to json
json_record=list(json.loads(df.T.to_json()).values())


#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)