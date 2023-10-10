# List of common functions used in MongoDB with Python (using the `pymongo` library)

1. `MongoClient()`: Establishes a connection to the MongoDB server.
2. `client.list_database_names()`: Lists the names of all databases on the server.
3. `db.list_collection_names()`: Lists the names of all collections in the current database.
4. `db.create_collection()`: Creates a new collection in the current database.
5. `db.collection.insert_one()`: Inserts a single document into the collection.
6. `db.collection.insert_many()`: Inserts multiple documents into the collection.
7. `db.collection.find()`: Retrieves documents from the collection based on a query.
8. `db.collection.find_one()`: Retrieves a single document from the collection based on a query.
9. `db.collection.update_one()`: Updates a single document in the collection.
10. `db.collection.update_many()`: Updates multiple documents in the collection.
11. `db.collection.delete_one()`: Deletes a single document from the collection.
12. `db.collection.delete_many()`: Deletes multiple documents from the collection.
13. `db.collection.aggregate()`: Performs aggregation operations on the collection's data.
14. `db.collection.count_documents()`: Counts the number of documents in the collection that match a query.
15. `db.collection.distinct()`: Retrieves distinct values for a specific field in the collection.
16. `db.collection.find_one_and_update()`: Atomically finds and updates a single document.
17. `db.collection.find_one_and_delete()`: Atomically finds and deletes a single document.
18. `db.collection.indexes.create_one()`: Creates a single index on the collection.
19. `db.collection.indexes.create_many()`: Creates multiple indexes on the collection.
20. `db.command()`: Executes a database command.