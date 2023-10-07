# Problem Statement - IXTL 
* To use the Zomato MongoDB database from the command line (CLI)
* This is just dummmy Zomato DB for Testing

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


# ERROR:

### If you are getting 'mongdb' is not recognized as an internal or external command, operable program or batch file.

Then follow these steps:

* The error message "'mongdb' is not recognized as an internal or external command, operable program or batch file" suggests that the `mongo` command-line tool is not in your system's PATH, which means the command prompt doesn't know where to find the `mongo` command. To resolve this issue, you can do the following:

1. **Check MongoDB Installation**: First, make sure you have MongoDB installed on your system.

2. **Add MongoDB Bin Directory to PATH**:

   - **Windows**:
     - Open the Start menu and search for "Environment Variables."
     - Click on "Edit the system environment variables."
     - In the "System Properties" window, click the "Environment Variables" button.
     - In the "System Variables" section, scroll down to find the "Path" variable and select it, then click "Edit..."
     - Click "New" and add the path to the "bin" directory of your MongoDB installation (e.g., `C:\Program Files\MongoDB\Server\4.4\bin`).
     - Click "OK" to close all the windows.

   - **Linux/macOS**:
     - Open your terminal.
     - Edit the `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc` file (depending on your shell configuration).
     - Add the following line to the file, replacing `/path/to/mongodb/bin` with the actual path to the MongoDB bin directory:

     ```bash
     export PATH=$PATH:/path/to/mongodb/bin
     ```

     - Save the file and exit.

3. **Restart Your Terminal**: Close and reopen your Command Prompt (Windows) or Terminal (Linux/macOS) to apply the changes.

4. **Try the `mongo` Command Again**: Now, try running the `mongo` command again in your terminal:

   ```bash
   mongo mongodb://username:password@hostname:port/zomato
   ```

Ensure you've replaced the placeholders with your actual MongoDB connection string information.

By adding the MongoDB bin directory to your PATH, your system will be able to locate and run the `mongo` command from any directory, and you should no longer encounter the "'mongdb' is not recognized" error.

