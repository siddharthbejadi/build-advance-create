# BAC (Build. Advance. Create.) - Pre-Launch Landing Page

This is the official pre-launch landing page for BAC (Bejadi A Consortium pvt ltd). Its purpose is to communicate our vision and capture email leads for our newsletter.

This project is built with Django and is configured for deployment on Heroku.

## Core Features

-   **Static Landing Page:** A modern, single-page site communicating the "Build. Advance. Create." vision.
    
-   **Newsletter Signup:** A robust email capture form.
    
-   **Database Integration:** Saves all subscribed emails directly to the Django database.
    
-   **Automatic Email:** Instantly sends a "Welcome" email to new subscribers via SendGrid.
    
-   **Admin Panel:** Allows you to view and manage the list of subscribed emails.
    

## Prerequisites

Before you begin, you will need the following installed on your machine:

-   Python 3.9+
    
-   Pip (Python package installer)
    
-   Git (for version control)
    
-   [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli "null") (for deployment)
    

## 1\. Local Setup Instructions

Follow these steps to get the project running on your local machine.

### A. Get the Code and Install Dependencies

1.  **Clone the repository:**
    
        git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
        cd your-repo-name
        
    
2.  **Create and activate a virtual environment:**
    
    -   On Windows:
        
            python -m venv env
            .\env\Scripts\activate
            
        
    -   On macOS/Linux:
        
            python3 -m venv env
            source env/bin/activate
            
        
3.  **Install all required packages:**
    
        pip install -r requirements.txt
        
    

### B. Configure Your Environment

This project will not run without proper configuration, especially for sending emails.

1.  **Open `bac_consortium/settings.py`**.
    
2.  **Set your SendGrid API Key:** Find the line `SENDGRID_API_KEY` and paste in your key from SendGrid.
    
        SENDGRID_API_KEY = 'PASTE_YOUR_API_KEY_HERE'
        
    
3.  **Set your Domain:**
    
    -   Find `DEFAULT_FROM_EMAIL` and change it to your verified email (e.g., `updates@build-advance-create.org`).
        
    -   Find `ALLOWED_HOSTS` and add `'127.0.0.1'` and `'localhost'` for local testing.
        
    
        ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
        DEFAULT_FROM_EMAIL = 'updates@build-advance-create.org'
        
    

### C. Set Up the Database

1.  **Run migrations** to create your local `db.sqlite3` database file:
    
        python manage.py makemigrations
        python manage.py migrate
        
    
2.  **Create a superuser** to access the Admin Panel:
    
        python manage.py createsuperuser
        
    
    (Enter a username, email, and password when prompted)
    

## 2\. Running the Application Locally

1.  **Start the development server:**
    
        python manage.py runserver
        
    
2.  **Open your browser:**
    
    -   **Website:** Go to `http://127.0.0.1:8000/`
        
    -   **Admin Panel:** Go to `http://127.0.0.1:8000/admin` (and log in with your superuser credentials).
        
3.  **Test the email sending:**
    
    -   Submit your email in the form.
        
    -   Check your terminal. Since `SENDGRID_ECHO_TO_STDOUT = True` is set, you should see the full text of the welcome email printed in your console.
        
    -   Check the Admin Panel to see your email saved in the "Subscribers" list.
        

## 3\. Deployment to Heroku

These are the commands to deploy your application to a live website.

1.  **Initialize Git (if not already done):**
    
        git init
        git add .
        git commit -m "Initial commit"
        git branch -m main  # Renames the branch to 'main'
        
    
2.  **Log in to Heroku and Create the App:**
    
        heroku login
        heroku create your-unique-app-name
        
    
    (If you let Heroku create a name, it will be added automatically. If you provide a name, you may need to add the remote manually.)
    
3.  **Set Heroku Configuration (CRITICAL):** Your app needs to know its live URL and its secret email key.
    
        # Replace with your app's actual Heroku URL
        heroku config:set HEROKU_HOSTNAME='your-unique-app-name.herokuapp.com'
        
        # Set your SendGrid key in the production environment
        heroku config:set SENDGRID_API_KEY='PASTE_YOUR_API_KEY_HERE'
        
    
4.  **Push Your Code to Deploy:**
    
        git push heroku main
        
    
5.  **Set Up the Production Database:** You must run migrations _on the Heroku server_ after your first deploy.
    
        heroku run python manage.py migrate
        
    
6.  **Open Your Live Site:**
    
        heroku open
        
    

## 4\. Other Useful Commands

-   **Backing up your code to GitHub:** (First, create an empty repository on GitHub)
    
        git remote add origin [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
        git push origin main
        
    
-   **Viewing live server logs on Heroku:** (Use this to see any errors on your live website)
    
        heroku logs --tail
