# Applying CSS to Navbar

1. Create a CSS file (e.g., `styles.css`) in your Flask app's `static` folder (create the folder if it doesn't exist already).

2. Add CSS styles to customize the navbar in your `styles.css` file. Here's an example of how you can style the navbar to make it more beautiful:

```css
/* styles.css */

/* Style the navbar */
.navbar {
    background-color: #333; /* Background color of the navbar */
    overflow: hidden;
}

/* Style the navbar links */
.navbar ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

.navbar li {
    float: left;
}

.navbar a {
    display: block;
    color: white; /* Text color of the links */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change link color on hover */
.navbar a:hover {
    background-color: #ddd; /* Background color on hover */
    color: black; /* Text color on hover */
}
```

3. Link the CSS file in your `layout.html` template inside the `<head>` section:

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
```

4. With these CSS styles, your navbar will have a dark background color (`#333`), white text, and a subtle hover effect.

