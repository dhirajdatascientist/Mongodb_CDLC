# To add CSS to your Flask application, 

* You can create a `static` folder in your project directory to store your CSS files. Here's how you can do it:

1. Create a `static` folder in your project directory.

2. Inside the `static` folder, create a CSS file, e.g., `styles.css`. You can define your CSS rules in this file.

```css
/* styles.css */

/* Example styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    color: #333;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
    background-color: #fff;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

form {
    margin-top: 20px;
}
```

3. Link the CSS file to your HTML templates. In your HTML templates (e.g., `layout.html`, `index.html`, and `booking.html`), add the following line inside the `<head>` section to include the CSS file:

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
```

Update your `layout.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Food Booking App</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Food Booking App</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

And you can also include it in your other HTML templates like `index.html` and `booking.html` by adding the same `<link>` tag.

4. Make sure the Flask application is running (`python app.py`), and your CSS styles should be applied to your web pages.
