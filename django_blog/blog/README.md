# Django Blog Authentication System

## Overview

This project includes a user authentication system for a Django blog application. It allows users to register, log in, log out, and manage their profiles.

## Features

- User registration with email
- User login and logout
- Profile management (view and edit profile details)

## Setup Instructions

1. **Clone the repository**:
    
    git clone https://github.com/sunmitechie/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/django_blog
    

2. **Run migrations**:
    
    python manage.py makemigrations
    python manage.py migrate
    

4. **Create a superuser**:
    
    python manage.py createsuperuser
    

5. **Run the development server**:
    
    python manage.py runserver
    

6. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000/`.

## Authentication Endpoints

- **Login**: `/login/`
- **Logout**: `/logout/`
- **Register**: `/register/`
- **Profile**: `/profile/`

## Testing

To test the authentication functionalities, use the following steps:

1. **Register a new user**:
    - Go to `/register/` and fill out the registration form.
    - Submit the form to create a new user.

2. **Log in**:
    - Go to `/login/` and enter your credentials.
    - Submit the form to log in.

3. **View and edit profile**:
    - Go to `/profile/` to view your profile details.
    - Edit the form and submit to update your profile.

4. **Log out**:
    - Click the logout link on the profile page to log out.

## Security

- All forms use CSRF tokens to protect against CSRF attacks.
- Passwords are handled securely using Django’s built-in hashing algorithms.