```
- File created by: Dhiraj Kr
- Topic: Connect(L1)
```

1. Click on connect
2. You will see
    - Databases
    - admin
    - config
    - local

**Explanation**

In MongoDB Compass, the steps you've described relate to connecting to a MongoDB server. Here's an explanation of what happens when you follow these steps:

1. **Click on Connect:**
   - When you open MongoDB Compass, you'll typically start on the Connect screen. This is where you initiate a connection to your MongoDB server.

2. **You will see:**
   - After clicking on Connect, the main part of the Compass interface will display the available databases on the connected MongoDB server. Here's what you'll typically see:

      - **Databases:** This section lists all the databases that exist on the MongoDB server to which you've connected. MongoDB can have multiple databases, and each database can contain collections of documents. Databases are used to organize data.

      - **admin:** This is a system database in MongoDB used for administrative purposes. It typically contains user authentication and management information.

      - **config:** Another system database, the config database is used for sharding configuration in MongoDB. It stores metadata about sharded clusters if you're using MongoDB in a sharded setup.

      - **local:** The local database is also a system database, and it stores data that is local to a specific MongoDB server. It's used for internal purposes and is not typically accessed directly by applications.

   These are some of the default system databases that are automatically created when you set up a MongoDB server. In addition to these, you may see other databases listed here if they have been created on your MongoDB server.

**Conclusion**
When you click on "Connect" in MongoDB Compass, you'll be presented with a list of databases available on the connected MongoDB server, which includes system databases like "admin," "config," and "local," as well as any user-created databases. You can click on a specific database to explore its collections and data.