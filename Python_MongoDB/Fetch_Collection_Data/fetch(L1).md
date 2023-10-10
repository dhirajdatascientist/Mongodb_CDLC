import pymongo

# MongoDB connection parameters
mongo_uri = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
database_name = "your_database_name"       # Replace with your database name
collection_name = "your_collection_name"   # Replace with your collection name

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# Fetch all documents from the collection
all_documents = collection.find()

# Iterate through the documents and print them
for document in all_documents:
    print(document)

# Close the MongoDB connection
client.close()
