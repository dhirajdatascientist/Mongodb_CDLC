import pymongo

mongo_host = "localhost"
mongo_port = 27017
mongo_db_name = "Infys"

client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
db = client[mongo_db_name]
if db is not None:
    print("Connected to MongoDB!")
    client.close()
else:
    print("Failed to connect to the database.")
