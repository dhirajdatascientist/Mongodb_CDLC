## Problem Statement:
```
Establish a connection to a MongoDB server and display a message when the connection is successful:
```

* To connect Python to MongoDB and display a message indicating that the connection is successful, you'll need to use the `pymongo` library, which is a Python driver for MongoDB. If you haven't already installed it, you can do so using pip:

```bash
pip install pymongo
```

## 1. Simple Code:

```python
import pymongo

# MongoDB connection parameters
mongo_host = "localhost"  # Replace with your MongoDB server hostname or IP address
mongo_port = 27017  # Default MongoDB port
mongo_db_name = "my_database"  # Replace with the name of your database


# Establish a connection to MongoDB
client = pymongo.MongoClient(host=mongo_host, port=mongo_port)

# Access the specified database (creates it if it doesn't exist)
db = client[mongo_db_name]

# Display a message indicating the successful connection
print("Connected to MongoDB!")

# Optionally, you can perform MongoDB operations here

# Close the connection when you're done
client.close()

```

## 2. Using If condition:

```Python
import pymongo

mongo_host = "localhost"
mongo_port = 27017
mongo_db_name = "my_database"

client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
db = client[mongo_db_name]
if db is not None:
    print("Connected to MongoDB!")
    client.close()
else:
    print("Failed to connect to the database.")

```
## 3. Using try and except:

```Python
import pymongo

mongo_host = "localhost"
mongo_port = 27017
mongo_db_name = "my_database"

try:
    client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    db = client[mongo_db_name]
    if db is not None:
        print("Connected to MongoDB!")
        client.close()
    else:
        print("Failed to connect to the database.")

except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")

```

**Explanation**


1. First, you need to import a Python library called "pymongo" to work with MongoDB databases.

2. You set some variables to store information about your MongoDB server. "mongo_host" is where your server is located (usually "localhost" if it's on your own computer), "mongo_port" is the port number MongoDB is using (usually 27017), and "mongo_db_name" is the name of the database you want to connect to (replace "my_database" with your actual database name).

3. Next, you create a "client" object using pymongo. This client will help you connect to the MongoDB server using the host and port you specified.

4. You create a "db" object by accessing the "mongo_db_name" from the "client" object. This "db" represents the specific database you want to work with.

5. You check if "db" is not None, which means the connection to the MongoDB database was successful.

6. If the connection is successful, you print "Connected to MongoDB!" to indicate that you've successfully connected to the database.

7. After printing the message, you close the "client" connection using "client.close()". This is good practice to close the connection when you're done using it.

8. If the connection to the database fails, you print "Failed to connect to the database."

9. Make sure to replace the placeholders like "localhost," "27017," and "my_database" with your actual MongoDB server details and database name.

10. Now, when you run this code, it will attempt to connect to your MongoDB database, and it will let you know if the connection was successful or not.