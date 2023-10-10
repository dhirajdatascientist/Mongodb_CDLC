from pymongo import MongoClient

# Connect to MongoDB (assuming it's running locally)
client = MongoClient('mongodb://localhost:27017/')

# Specify the database and collection name
db_name = 'Infy'
collection_name = 'mycollection'

# Access the database and collection
db = client[db_name]
collection = db[collection_name]

# Define the filter to find the document with name "Ram"
filter_criteria = {"name": "Ram"}

# Define the update operation to add the phone number
update_operation = {
    "$set": {
        "phone": "9901"
    }
}

# Update the document matching the filter
result = collection.update_one(filter_criteria, update_operation)

# Check if a document was updated
if result.modified_count > 0:
    print("Phone number added to the document successfully.")
else:
    print("No document found with the name 'Ram'.")

# Close the MongoDB connection
client.close()
