# Requirements
To connect Python code to a MongoDB database and display a "Connection successful" message, you can use the `pymongo` library, which is a Python driver for MongoDB. Make sure you have `pymongo` installed, which you can do using `pip`:

```bash
pip install pymongo
```

Here's a Python code example that establishes a connection to a MongoDB database and displays a "Connection successful" message if the connection is established successfully:

```python
import pymongo

# Replace these variables with your MongoDB connection details
mongodb_uri = "mongodb://username:password@host:port/database_name"

try:
    # Attempt to connect to the MongoDB server
    client = pymongo.MongoClient(mongodb_uri)

    # Access a sample collection to ensure the connection is successful
    db = client.get_database()
    sample_collection = db.get_collection("sample_collection")

    # If the connection is successful, print a message
    print("Connection to MongoDB successful!")

except pymongo.errors.ConnectionFailure as e:
    # If there is an error connecting to MongoDB, print an error message
    print("Connection to MongoDB failed: %s" % e)
```

Make sure to replace `"mongodb://username:password@host:port/database_name"` with your actual MongoDB connection string, including your credentials and database details.

When you run this code, it will attempt to connect to your MongoDB database. If the connection is successful, it will print "Connection to MongoDB successful!" to the console. If there's an error in the connection, it will print an error message.