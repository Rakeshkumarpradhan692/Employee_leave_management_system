# Leave Management System

A Django-based Leave Management System for employees and administrators to manage leave applications efficiently.

used technology-
html,
css,
javascript,
python,
Django,
Dbsqlites(Database)

---

## Features

- Employee sign up and login then apply for leave,and cheak the status of applying leaves and can see all the leaves apply by him/her.
- Admin dashboard for approving or rejecting leave requests(admin can sign up by create super user command)
- Secure authentication with custom user roles

---

## Requirements

- Python 3.8 or higher
- Django 4.0 or higher
- A virtual environment tool (e.g., `venv` or `virtualenv`)

---

## Installation and Setup

cd leave-management-system
python manage.py makemigrations
python manage.py migrate

to create super user for admin- python manage.py createsuperuser
