In MongoDB, you can use the `$and` and `$or` operators to perform logical AND and OR operations in queries to filter documents based on multiple conditions.


**Logical AND (`$and`):**
The `$and` operator allows you to find documents that satisfy all specified conditions. It's used to combine multiple conditions, and a document must meet all of them to be included in the result.

```python
query = {
    "$and": [
        {"age": {"$gte": 18}},  # Age is greater than or equal to 18
        {"city": "New York"}    # City is "New York"
    ]
}
result = collection.find(query)
```

In the above example, the query will retrieve documents where both conditions (age greater than or equal to 18 and city is "New York") are true.

**Logical OR (`$or`):**
The `$or` operator allows you to find documents that satisfy at least one of the specified conditions. It's used to combine multiple conditions, and a document must meet at least one of them to be included in the result.

```python
query = {
    "$or": [
        {"age": {"$gte": 18}},  # Age is greater than or equal to 18
        {"city": "New York"}    # City is "New York"
    ]
}
result = collection.find(query)
```

In the above example, the query will retrieve documents where either the age is greater than or equal to 18 or the city is "New York."

You can also nest these operators to create more complex queries. For example, combining `$and` and `$or`:

```python
query = {
    "$and": [
        {"$or": [{"age": {"$gte": 18}}, {"city": "New York"}]},  # Age is 18+ or City is "New York"
        {"hobbies": "Reading"}                                   # Hobbies include "Reading"
    ]
}
result = collection.find(query)
```

This query will retrieve documents where either the age is greater than or equal to 18 or the city is "New York," and the hobbies include "Reading."