# 🧶 The Crochet Files

## 🚀 Deployment 

🚀 Deploying the crochet-files Django App to Heroku
Note: These instructions assume you have a verified Heroku account and an Eco Dynos plan via the GitHub Student Developer Pack.

🛠️ 1. Create a New Heroku App
Go to your Heroku Dashboard and click "New" > "Create new app".

Choose a unique app name and region, then click "Create app".

⚙️ 2. Configure Environment Variables
In your app dashboard, go to the Settings tab.

Click "Reveal Config Vars".

Add the following key-value pair:

Key: DISABLE_COLLECTSTATIC

Value: 1

Click Add.

This disables automatic static file collection during deployment, which we’ll configure manually later when HTML/CSS are in place.

🔧 3. Install a Production Web Server
Install Gunicorn:

Run pip3 install gunicorn~=20.1.

Add it to your requirements.txt:

Run pip3 freeze --local > requirements.txt.

Gunicorn is a production-ready WSGI server, replacing runserver for live environments.

📁 4. Create a Procfile
At the root of your project directory (same level as requirements.txt), create a file named Procfile (no extension).

Inside, add:

web: gunicorn my_project.wsgi

Replace my_project with your Django project’s actual name (the one with settings.py).

🔒 5. Update Django Settings
Open settings.py and make the following changes:

a. Add Heroku to Allowed Hosts:

ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']

Adjust the list if you see a DisallowedHost error with a different address.

b. Turn off Debug Mode:

DEBUG = False

Required for security in production environments.

💾 6. Commit and Push Changes to GitHub
Run git add .

Run git commit -m "Prepare project for Heroku deployment"

Run git push.

🌐 7. Connect GitHub to Heroku
Go back to your Heroku app dashboard and open the Deploy tab.

Under Deployment Method, select GitHub and click Connect to GitHub.

Search for your repository by name, then click Connect.

🚀 8. Deploy the App
Scroll to the bottom of the Deploy page and click Deploy Branch.

Wait for the build to complete. You can monitor progress under the Activity tab.

⚙️ 9. Set Up Dyno and Remove Postgres
Go to the Resources tab.

Ensure at least one Eco Dyno is enabled.

If there's a Heroku Postgres add-on (not needed for this project), click the three dots next to it and choose Delete Add-on.

🌍 10. View Your Live App
Click Open app at the top-right of your dashboard.

