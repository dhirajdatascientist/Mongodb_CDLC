## `find()` method in MongoDB 

1. **Basic Find:**
## Retrieve all documents from the collection
```python
result = collection.find()  
```

2. **Filter by Field Value:**
## Find documents where the "name" field is "Alice"

```python
query = {"name": "Alice"}  
result = collection.find(query)
   ```

3. **Filter by Field Value and Projection:**
## Find documents where the "age" field is greater than or equal to 25

```python
query = {"age": {"$gte": 25}}  
projection = {"name": 1, "age": 1}  # Include only "name" and "age" fields in the result
result = collection.find(query, projection)
```

4. **Sorting Documents:**
## Sort documents by "age" in ascending order
   ```python
   result = collection.find().sort("age", pymongo.ASCENDING)  
   ```

5. **Limit and Skip for Pagination:**
## Retrieve 10 documents, skipping the first 20

```python
result = collection.find().limit(10).skip(20)  
```

6. **Filter Using Logical Operators:**
## Find documents where "name" is "Alice" or "Bob"
```python
query = {"$or": [{"name": "Alice"}, {"name": "Bob"}]}  
result = collection.find(query)
```

7. **Filter by Array Elements:**
## Find documents where "hobbies" array contains "Gaming"

```python
query = {"hobbies": "Gaming"}  
result = collection.find(query)
```


8. **Filter by Date Range:**
## Find documents with a birth date on or after 1990-01-01

```python
import datetime
query = {"birth_date": {"$gte": datetime.datetime(1990, 1, 1)}}  
result = collection.find(query)
```



9. **Using Regular Expressions (Regex):**
## Find documents where "name" starts with 'A'
    
```python
import re
query = {"name": {"$regex": re.compile("^A")}}  
result = collection.find(query)
```

10. **Compound Query:**
## Find documents where age is 25+ and hobbies include "Reading"

```python
query = {"$and": [{"age": {"$gte": 25}}, {"hobbies": "Reading"}]}  
result = collection.find(query)
```
