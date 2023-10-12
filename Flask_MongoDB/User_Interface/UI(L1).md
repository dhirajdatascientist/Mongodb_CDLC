## Develop a user interface that interacts with MongoDB using Flask.

## Requirements:
1. Flask
2. Flask-PyMongo
3. WTForms

You can install these with pip:

```bash
pip install Flask Flask-PyMongo WTForms
```

## Simple Flask Application with MongoDB:

### 1. Setting up the Flask App:
**app.py**

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

if __name__ == "__main__":
    app.run(debug=True)
```

### 2. Creating the templates:

**templates/index.html**

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
            <li>{{ user['name'] }}</li>
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

### 3. Running the application:

1. Ensure you have MongoDB running on your local machine.
2. Run the Flask application:

```bash
python app.py
```

3. Visit http://127.0.0.1:5000/ in your browser to see the application in action.

This is a basic example. You can expand this by adding features like updating, deleting users, and handling more complex forms. Always remember to handle user inputs securely and avoid direct database operations without validation to prevent potential issues like NoSQL injection.