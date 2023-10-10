# Add a navigation bar (navbar) to your Flask application

* You can modify your `layout.html` file to include navigation links. 

1. Update your `layout.html` to include a navbar with links. Here's an example of a  navbar with two links for your food booking app:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Food Booking App</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <nav class="navbar">
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
        </ul>
    </nav>
    <h1>Food Booking App</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

In this example, we've added a `nav` element with an unordered list (`ul`) containing list items (`li`) for each navigation link. The links use Flask's `url_for` function to generate URLs for the 'index' and 'about' routes. You can modify the links and their URLs to match the routes in your application.

2. Next, you can add an 'About' page route to your Flask application. Modify your `app.py`:

```python
# ... (previous code)

# Define the 'about' route
@app.route('/about')
def about():
    return render_template('about.html')

# ... (remaining code)
```

3. Create an `about.html` template in your `templates` folder to display content for the 'About' page:

```html
{% extends 'layout.html' %}

{% block content %}
    <h2>About Us</h2>
    <p>This is the about page for our food booking app.</p>
{% endblock %}
```

4. Finally, make sure your Flask application is running (`python app.py`), and you should see the navbar with 'Home' and 'About' links. Clicking on these links should navigate you to the respective pages.

