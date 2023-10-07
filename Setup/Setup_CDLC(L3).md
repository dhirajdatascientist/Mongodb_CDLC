# Problem Statement - IXTL 
* Forgotten the password of admin
```

📁 File Created by : Dhiraj
📧 Gmail  : dhiraj.datascientist@gmail.com 
👨‍💻 Github : dhirajdatascientist
```

If you're trying to reset the password for the MongoDB admin user and you've forgotten the admin password, you'll need to follow a different approach. Here's how you can reset the admin password:

1. **Stop MongoDB**: First, you should stop the MongoDB server. You can do this using the following command:

   - On Windows:

     ```bash
     net stop MongoDB
     ```

   - On Linux/macOS:

     ```bash
     sudo service mongod stop
     ```

2. **Start MongoDB in Maintenance Mode**: You'll need to start MongoDB in maintenance mode to bypass authentication. To do this, open a terminal or command prompt and run MongoDB with the `--noauth` option:

   - On Windows:

     ```bash
     mongod --dbpath /path/to/data/db --noauth
     ```

   - On Linux/macOS:

     ```bash
     sudo mongod --dbpath /path/to/data/db --noauth
     ```

   Replace `/path/to/data/db` with the actual path to your MongoDB data directory.

3. **Connect to MongoDB**: Open another terminal or command prompt and connect to the MongoDB server without authentication by running the `mongo` command:

   ```bash
   mongo
   ```

4. **Switch to the `admin` Database**: After connecting to MongoDB, switch to the `admin` database:

   ```javascript
   use admin
   ```

5. **Create a New Admin User**: Now that you're in the `admin` database, you can create a new admin user with a new password using the `db.createUser()` command. Replace `newadmin` with the desired admin username and `newpassword` with the new password:

   ```javascript
   db.createUser({
     user: "newadmin",
     pwd: "newpassword",
     roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
   })
   ```

6. **Exit the MongoDB Shell**: Type `exit` and press Enter to exit the MongoDB shell.

7. **Stop MongoDB**: In the terminal or command prompt where MongoDB is running in maintenance mode, stop the server by pressing `Ctrl + C`.

8. **Restart MongoDB Normally**: Start MongoDB as you normally would without the `--noauth` option:

   - On Windows:

     ```bash
     net start MongoDB
     ```

   - On Linux/macOS:

     ```bash
     sudo service mongod start
     ```

Now, you should have reset the admin password to the new password you specified ("newpassword" in the example). You can connect to MongoDB with the new admin credentials. Please ensure that you replace "newadmin" and "newpassword" with your desired username and password.