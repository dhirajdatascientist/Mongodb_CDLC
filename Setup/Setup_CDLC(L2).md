# Problem Statement - IXTL 
* To reset the password for a MongoDB user

```
File Created by : Dhiraj
Gmail  : dhiraj.datascientist
Github : dhirajdatascientist
```

# Steps

1. **Access MongoDB Shell**: Open a terminal or command prompt and start the MongoDB shell by running the `mongo` command with the appropriate connection string. Replace the placeholders with your actual MongoDB connection information:

   ```bash
   mongo mongodb://username:password@hostname:port/admin
   ```

   Make sure you connect to the `admin` database or a database where you have user management privileges.

2. **Switch to the `admin` Database**: If you're not already in the `admin` database, switch to it using the `use admin` command:

   ```javascript
   use admin
   ```

3. **List Existing Users**: To see the list of existing users, run the following command:

   ```javascript
   db.getUsers()
   ```

   This command will display the user accounts in the `admin` database.

4. **Reset User Password**: To reset the password for a specific user, use the `db.changeUserPassword()` method. Replace `username` with the username of the user whose password you want to reset and provide the new password in plain text:

   ```javascript
   db.changeUserPassword("username", "new_password")
   ```

   Replace `"username"` with the actual username and `"new_password"` with the desired new password. Note that you should enclose the username in double quotes.

   For example, if you want to reset the password for a user named "myuser" to "newpassword," you would run:

   ```javascript
   db.changeUserPassword("myuser", "newpassword")
   ```

5. **Exit the MongoDB Shell**: Type `exit` and press Enter to exit the MongoDB shell.

6. **Restart MongoDB**: If you've made changes to user passwords, you may need to restart your MongoDB server for the changes to take effect.

After following these steps, the password for the specified MongoDB user should be reset to the new password you provided. Make sure to update any application configurations that use this MongoDB user with the new password.