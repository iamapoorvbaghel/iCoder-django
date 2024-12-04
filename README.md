iCoder is a blog website built using the Django framework. It allows users to read, write, and comment on blog posts. The website features user authentication, user profiles, and a rich text editor for creating blog content.

Features
User authentication (signup, login, logout)

User profiles

Create, read, update, and delete blog posts

Comment on blog posts

Rich text editor for writing posts

Responsive design

Installation
Prerequisites
Python 3.x

Django 3.x

PostgreSQL (or any other preferred database)

Virtualenv (optional but recommended)

Step-by-Step Instructions
Clone the Repository

sh
git clone https://github.com/your-username/icoder.git
cd icoder
Create a Virtual Environment

sh
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install Dependencies

sh
pip install -r requirements.txt
Database Setup

Make sure PostgreSQL (or your preferred database) is installed and running.

Create a database for the project.

Update the DATABASES setting in settings.py with your database credentials.

Run Migrations

sh
python manage.py makemigrations
python manage.py migrate
Create a Superuser

sh
python manage.py createsuperuser
Run the Development Server

sh
python manage.py runserver
Access the Website

Open your web browser and go to http://127.0.0.1:8000/ to access the iCoder website.

Usage
Sign Up

Register for a new account by clicking the Sign Up link.

Confirm your email address (if email verification is enabled).

Log In

Log in to your account using your credentials.

Create a New Post

Click on "New Post" and use the rich text editor to create your blog post.

Save and publish your post.

View and Comment on Posts

Browse through existing blog posts.

Add comments to posts you are interested in.

Manage Your Profile

Update your user profile information.

Configuration
Environment Variables:

Configure environment variables for sensitive information such as database credentials, secret key, etc., in a .env file or directly in your system environment variables.

Technology Stack
Backend: Django

Database: PostgreSQL (or your preferred database)

Frontend: HTML, CSS, JavaScript

Editor: Rich text editor (like TinyMCE or CKEditor)

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

Fork the repository

Create a new branch (git checkout -b feature-branch)

Make your changes

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature-branch)

Create a new Pull Request
