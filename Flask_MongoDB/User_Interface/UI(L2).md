### Expand the application by adding a delete operation and also an update operation for the users.

### 1. Updating the Flask App:

Modify **app.py** to incorporate the delete and update functionalities:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from wtforms import StringField, Form

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"

mongo = PyMongo(app)

class UserForm(Form):
    name = StringField('Name')

@app.route('/')
def index():
    users = mongo.db.users.find()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        mongo.db.users.insert_one({'name': name})
        flash('User added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form.get('name')
    mongo.db.users.update_one({'_id': ObjectId(user_id)}, {"$set": {'name': name}})
    flash('User updated successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    flash('User deleted successfully!', 'success')
    return redirect(url_for('index'))

from bson.objectid import ObjectId  # Required to convert string representation of ObjectId to actual ObjectId

if __name__ == "__main__":
    app.run(debug=True)
```

### 2. Updating the template:

Modify **templates/index.html** to provide delete and update functionalities:

```html
<!DOCTYPE html>
<html>
<head>
    <title>MongoDB with Flask</title>
</head>
<body>
    <h2>Add User</h2>
    <form method="post" action="/add_user">
        <input type="text" name="name" placeholder="Enter Name" required>
        <input type="submit" value="Add">
    </form>

    <h2>Users List:</h2>
    <ul>
        {% for user in users %}
            <li>
                {{ user['name'] }}
                <form method="post" action="/update_user/{{ user['_id'] }}" style="display:inline;">
                    <input type="text" name="name" placeholder="New Name">
                    <input type="submit" value="Update">
                </form>
                <a href="/delete_user/{{ user['_id'] }}">Delete</a>
            </li>
        {% endfor %}
    </ul>

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
</body>
</html>
```

In this updated template, each user has an input field for updating the name, an update button, and a delete link next to their name. The delete link will remove the user from the database, while the update button will modify the user's name.
