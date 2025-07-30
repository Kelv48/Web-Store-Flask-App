# Web Store Flask App

This is a Flask-based web application that allows users to buy products or services, to wishlist and rate items.
It includes user authetication and profile feautures, it also has the ability for an admin account to add new products/services or for the admin to manage orders and moderate reviews.
The admin account can also see all the ongoing projects and can see all the current employess and can add and remove them at will.

## Technologies Used
<ul>
<li>Python (Version 3.10.9)</li>
<li>Flask (Web Framework)</li>
<li>SQLite (Database for storing data)</li>
<li>HTML/CSS (For front-end interface)</li>
<li>Flask_wtf (WTForms functionality)</li>
<li>WTForms (Form handling)</li>
<li>Werkzeug (Security Utilities)</li>
</ul>

## How to Run
<b>Have docker installed and configured 'docker build -t my-flask-app .'</b>
<b>Run the docker container 'docker run -p 5000:5000 my-flask-app'</b>
<b>Open 'http://127.0.0.1:5000/' in your browser</b>

## Feautures
<ul>
<li>User authentication (signup, login, logout)</li>
<li>Product/Service/Employee management (Add, update, delete)</li>
<li>A profile which complies all orders reviews and wishlisted items belonging to user</li>
<li>The ability to buy products or services</li>
<li>Search Functionality </li>
</ul>

<h2>Project Structure</h2>
<pre>
<code>
/flask_Session
│
├── /static
│   ├── /images
│   │   ├── empty_star.jpg
│   │   ├── favicon.ico
│   │   ├── star.png
│   └── styles.css
│
├── /templates
│   ├── about.html
│   ├── admin_orders.html
│   ├── admin_support.html
│   ├── all_employees.html
│   ├── base.html
│   ├── blog.html
│   ├── cart.html
│   ├── catalog.html
│   ├── catalog_management.html
│   ├── checkout.html
│   ├── employees.html
│   ├── employee_management.html
│   ├── employee_new.html
│   ├── faq.html
│   ├── index.html
│   ├── my_profile.html
│   ├── my_profile_setup.html
│   ├── my_account.html
│   ├── orders.html
│   ├── product_management.html
│   ├── products_new.html
│   ├── product_update.html
│   ├── products.html
│   ├── research.html
│   ├── research_new.html
│   ├── service_new.html
│   ├── sign_in_status.html
│   ├── support.html
│   └── wishlist.html
│
├── .flaskenv
├── app.db
├── app.py
├── database.py
├── forms.py
├── requirements.txt
├── run.py
└── schema.sql
</code>
</pre>

### Explanation of the Project Structure:

- **`/static`**: Contains static files like images and styles.
  - **`/images`**: Folder containing image files.
    - `empty_star.jpg`: An image file.
    - `favicon.ico`: The favicon for the website.
    - `star.png`: Another image file.
  - `styles.css`: The CSS file for styling the web app.
  
- **`/templates`**: Contains all HTML template files.
  - Various HTML files for different views in the app.
- **`app.db`**: The database.
- **`app.py`**: The flask app itself and all its functions.
- **`forms.py`**: All the wtforms for the flask app.
- **`schema.sql`**: All the SQL queries for the setting up of and inserting data into the db on launch
