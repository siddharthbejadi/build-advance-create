# BAC (Build. Advance. Create.) - Pre-Launch Landing Page

This is the official pre-launch landing page for BAC (Bejadi A Consortium pvt ltd). Its purpose is to communicate our vision and capture email leads for our newsletter.

This project is built with Django on an **ASGI** server (Uvicorn), making it scalable and ready for future real-time AI features. It is configured for secure deployment on Heroku using environment variables.

## Core Features

-   **Static Landing Page:** A modern, single-page site communicating the "Build. Advance. Create." vision.
    
-   **Newsletter Signup:** A robust email capture form that saves subscribers to the database.
    
-   **Automatic Email:** Instantly sends a "Welcome" email to new subscribers via SendGrid.
    
-   **Admin Panel:** Allows you to view and manage the list of subscribed emails.
    
-   **Production-Ready:** Uses ASGI (Uvicorn) for high performance and `python-dotenv` for secure key management.
    

## Prerequisites

Before you begin, you will need the following installed on your machine:

-   Python 3.9+
    
-   Pip (Python package installer)
    
-   Git (for version control)
    
-   [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli "null") (for deployment)
    

## Key Project Files

Ensure these files exist in your project's root directory (`/bac_project/`).

**`requirements.txt`** (Your list of dependencies)

    django
    uvicorn
    django-sendgrid-v5
    python-dotenv
    

**`Procfile`** (Your Heroku command to start the ASGI server)

    web: uvicorn bac_consortium.asgi:application --host 0.0.0.0 --port $PORT
    

**`.gitignore`** (Files to keep private and not upload)

    # Ignore the secret keys file
    .env
    
    # Ignore the local database
    db.sqlite3
    
    # Ignore Python virtual environment
    env/
    

**`.env`** (Your **PRIVATE** file for secret keys - **DO NOT COMMIT THIS FILE**)

    # This file stores your secret keys.
    SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxx
    

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
        
    

### B. Configure Your Environment (The `.env` file)

This project securely loads secrets from a `.env` file.

1.  **Create the `.env` file** in the root of your project (at the same level as `manage.py`).
    
2.  **Open the `.env` file** and add your SendGrid API key:
    
        SENDGRID_API_KEY=PASTE_YOUR_API_KEY_HERE
        
    
3.  **Create the `.gitignore` file** (as shown above) to ensure you never accidentally upload your `.env` file.
    

Your `settings.py` file is already configured to read this key automatically.

### C. Set Up the Database

1.  **Run migrations** to create your local `db.sqlite3` database file:
    
        python manage.py makemigrations
        python manage.py migrate
        
    
2.  **Create a superuser** to access the Admin Panel:
    
        python manage.py createsuperuser
        
    
    (Enter a username, email, and password when prompted)
    

## 2\. Running the Application Locally

You can run the site in two ways.

### A. Standard Development Server (Easy)

This is the standard Django way to test.

    python manage.py runserver
    

### B. Production Server (Advanced)

This command runs your site using the exact same `uvicorn` server that Heroku will use. It's a great way to do a final test.

    uvicorn bac_consortium.asgi:application --host 127.0.0.1 --port 8000 --reload
    

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
        
    
3.  **Set Heroku Configuration (CRITICAL):** Your app needs to know its live URL and its secret email key.
    
        # Replace with your app's actual Heroku URL
        heroku config:set HEROKU_HOSTNAME='your-unique-app-name.herokuapp.com'
        
        # Set your SendGrid key in the production environment
        # This securely copies your key to the Heroku server
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
