from pymongo import MongoClient

# Connect to MongoDB (assuming it's running locally)
client = MongoClient('mongodb://localhost:27017/')

# Specify the database and collection name
db_name = 'mydb'
collection_name = 'mycollection'

# Access the database and collection
db = client[db_name]
collection = db[collection_name]

# Count the number of documents in the collection
document_count = collection.count_documents({})

# Calculate the storage size of the collection in bytes
storage_size_bytes = db.command('collstats', collection_name)['storageSize']

print(f"Number of Documents in {collection_name}: {document_count}")
print(f"Storage Size of {collection_name} (Bytes): {storage_size_bytes}")
