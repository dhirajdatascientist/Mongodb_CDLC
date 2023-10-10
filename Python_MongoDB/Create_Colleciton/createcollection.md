## To create a collection in MongoDB

```python
import pymongo

# Connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access a database
mydb = client["mydatabase"]

# Create a collection (if it doesn't exist)
mycol = mydb["mycollection"]

# Check if the collection was created
if "mycollection" in mydb.list_collection_names():
    print("Collection 'mycollection' created successfully!")
else:
    print("Collection creation failed.")

# Close the MongoDB connection
client.close()
```
