from pymongo import MongoClient

# Connect to MongoDB (assuming it's running locally)
client = MongoClient('mongodb://localhost:27017/')

# Specify the database and collection name
db_name = 'Infy'
collection_name = 'mycollection'

# Access the database and collection
db = client[db_name]
collection = db[collection_name]

# Define the filter to find the document with name "John"
filter_criteria = {"name": "John Doe"}

# Define the update operation to change the name to "Ram"
update_operation = {"$set": {"name": "Ram"}}

# Update the first document matching the filter
result = collection.update_one(filter_criteria, update_operation)

# Check if a document was updated
if result.modified_count > 0:
    print("Document updated successfully.")
else:
    print("No document found with the name 'John'.")

# Close the MongoDB connection
client.close()
