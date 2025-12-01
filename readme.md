# Flask E-Commerce Application

This repository contains a mini e-commerce web application built for the **"Script Programming in Python"** course.  
The project demonstrates how to build a full-stack web app using:

- Python 3 (Object-Oriented)
- Flask
- MySQL
- Semantic UI (frontend styling)
- HTML templates (Jinja2)
- Session-based authentication and cart

---

## Project Overview

The application simulates a basic online store:

- Users can **register** and **log in**
- Products are loaded **from a MySQL database**
- Users can **add products to a cart**, **remove items**, and **checkout**
- During checkout, an **order** is created and stored in the database
- The app shows a personalized **"Thank you, \<User\>"** message after a successful order
- Logged-in users can **log out**, and the navbar updates based on session state

This project was designed to practice **Script programming in Python** with a focus on:

- Object-Oriented Programming (OOP)
- Database connectivity
- Web routing and templates
- State management using sessions

---

##  Technologies Used

- **Language:** Python 3.x  
- **Web Framework:** Flask  
- **Database:** MySQL (accessed via `mysql-connector-python`)  
- **Frontend:** HTML, Semantic UI (via CDN)  
- **Template Engine:** Jinja2  
- **Version Control:** Git + GitHub  

---

##  Project Structure

```text
python-ecommerce-flask/
├── app/
│   ├── __init__.py         # Flask app factory, session config
│   ├── database.py         # MySQL connection helper
│   ├── models.py           # OOP models: Product, User, Order
│   ├── routes.py           # All application routes (views)
│   └── templates/          # HTML templates (Jinja2)
│       ├── base.html       # Layout, navbar, Semantic UI includes
│       ├── index.html      # Product catalog page (home)
│       ├── cart.html       # Shopping cart page
│       ├── login.html      # Login form
│       ├── register.html   # Registration form
│       └── order_success.html # Order confirmation page
├── run.py                  # Entry point to run Flask app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
