To add a "Delete" button for bookings in the `booking.html` template. 

Modify the template as follows:

```html
{% extends 'layout.html' %}

{% block content %}
    <h2>Book a Table</h2>
    <form method="POST" action="{{ url_for('book', restaurant_id=restaurant_id) }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required>
        <br>
        <button type="submit">Book Now</button>
    </form>
    
    {% if bookings %}
        <h2>Bookings for this restaurant:</h2>
        <ul>
            {% for booking in bookings %}
                <li>
                    {{ booking.name }} - {{ booking.date }}
                    <form method="POST" action="{{ url_for('delete_booking', booking_id=booking._id) }}" style="display: inline;">
                        <button type="submit" onclick="return confirm('Are you sure you want to delete this booking?')">Delete</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
    {% endif %}
{% endblock %}
```

In the modified `booking.html` template, we added a section to display bookings for the restaurant, and for each booking, there's a "Delete" button. When the "Delete" button is clicked, it submits a form to a route named `delete_booking` with the `booking_id` as a parameter.

Now, you need to update your `app.py` file to handle the deletion of bookings. Add the following route and function to your `app.py`:

```python
# ...

@app.route('/delete_booking/<booking_id>', methods=['POST'])
def delete_booking(booking_id):
    booking = mongo.db.bookings.find_one_and_delete({'_id': ObjectId(booking_id)})
    if booking:
        return redirect(url_for('book', restaurant_id=booking['restaurant_id']))
    else:
        return "Booking not found.", 404

# ...
```

Make sure to import `ObjectId` from `bson` at the beginning of your `app.py` file:

```python
from bson import ObjectId
```
