# Problem Statement - IXTL 
* To use the Zomato MongoDB database from the command line (CLI)

```
File Created by : Dhiraj
Gmail  : dhiraj.datascientist
Github : dhirajdatascientist
```

1. Open a Command Prompt or Terminal window on your computer.

2. Make sure you have the MongoDB command-line tools installed. If not, you can download and install MongoDB from the official MongoDB website: https://www.mongodb.com/try/download/community

3. Once MongoDB is installed and running, you can connect to the Zomato database using the `mongo` command followed by the connection string. The connection string typically includes information about the server, port, and authentication credentials. It should look something like this:

```bash
mongo mongodb://username:password@hostname:port/zomato
```

Replace the following placeholders in the connection string with your actual information:

- `username`: Your MongoDB username
- `password`: Your MongoDB password
- `hostname`: The hostname or IP address where MongoDB is running
- `port`: The MongoDB port (usually 27017 by default)
- `zomato`: The name of the Zomato MongoDB database

For example, if your MongoDB username is `myuser`, your password is `mypassword`, MongoDB is running on `localhost`, and the Zomato database is named `zomato`, you would run a command like this:

```bash
mongo mongodb://myuser:mypassword@localhost:27017/zomato
```

4. After running the `mongo` command with the connection string, you should be connected to the Zomato database in the MongoDB shell. You can now execute MongoDB queries and commands as needed.

Here are some common MongoDB shell commands:

- `show dbs`: List all databases.
- `use zomato`: Switch to the Zomato database.
- `show collections`: List all collections in the current database.
- `db.collectionName.find()`: Query documents in a specific collection (replace `collectionName` with the actual collection name).

Remember to replace `collectionName` with the name of the specific collection you want to work with.

5. Once you've executed your MongoDB commands, you can exit the MongoDB shell by typing `exit`.
