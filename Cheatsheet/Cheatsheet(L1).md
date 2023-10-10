# MongoDB cheatsheet for common operations using Python and the `pymongo` library:

### Connecting to MongoDB

```python
from pymongo import MongoClient

# Connect to MongoDB (assuming it's running locally)
client = MongoClient('mongodb://localhost:27017/')
```

### Databases and Collections

```python
# Access a database
db = client['mydb']

# Create a new collection
collection = db['mycollection']

# List all database names
client.list_database_names()

# List all collection names in the current database
db.list_collection_names()

# Create a new collection with options (e.g., capped collection)
db.create_collection('mycollection', capped=True, size=100000)
```

### Inserting Data

```python
# Insert a single document
data = {"name": "John", "age": 30}
collection.insert_one(data)

# Insert multiple documents
data_list = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]
collection.insert_many(data_list)
```

### Querying Data

```python
# Find documents that match a query
result = collection.find({"name": "John"})

# Find a single document
result = collection.find_one({"name": "John"})

# Query with projection (return specific fields)
result = collection.find({}, {"_id": 0, "name": 1, "age": 1})

# Query with conditions (e.g., age greater than 25)
result = collection.find({"age": {"$gt": 25}})
```

### Updating Data

```python
# Update a single document
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# Update multiple documents
collection.update_many({"age": {"$gt": 30}}, {"$set": {"status": "senior"}})
```

### Deleting Data

```python
# Delete a single document
collection.delete_one({"name": "John"})

# Delete multiple documents
collection.delete_many({"age": {"$lt": 30}})
```

### Aggregation

```python
# Perform aggregation operations
pipeline = [
    {"$match": {"age": {"$gte": 25}}},
    {"$group": {"_id": "$name", "avg_age": {"$avg": "$age"}}}
]
result = collection.aggregate(pipeline)
```

### Indexing

```python
# Create a single index
collection.create_index([("name", 1)])

# Create multiple indexes
collection.create_indexes([
    [("name", 1)],
    [("age", -1)]
])
```

### Miscellaneous

```python
# Count documents that match a query
count = collection.count_documents({"age": {"$gt": 25}})

# Distinct values for a field
distinct_values = collection.distinct("name")

# Run a database command
result = db.command({"dbStats": 1})
```

