# Googlesheet-Django
Projeteminou is a Django-based web application designed for managing and viewing entries stored in a Google Sheet. The application includes functionalities to add, edit, delete, and search entries. It integrates Google Sheets using the gspread API, enabling seamless data management in the cloud.

Features
View and manage entries in a tabular format.
Add new entries through a form.
Edit existing entries.
Delete entries with confirmation prompts.
Search for entries based on specific criteria.
Integration with Google Sheets for storing data.
Table of Contents
Installation
Configuration
Usage
Google Sheets Integration
Screenshots
Contributing
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/projeteminou.git
cd projeteminou
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up Django:

bash
Copy code
python manage.py migrate
Configuration
Google Sheets API Setup:
To use Google Sheets, create a new project in the Google Cloud Console.
Enable the Google Sheets API and Google Drive API.
Download the credentials.json file for your project and place it in the root directory of the project.
Django Settings:
Update your settings.py file as necessary.
Ensure the gspread integration is configured to connect to your Google Sheets instance.
Usage
Run the development server:

bash
Copy code
python manage.py runserver
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:8000/
From the homepage, you can:

View entries.
Add, edit, or delete entries from the Google Sheet.
Google Sheets Integration
The project uses gspread for interacting with Google Sheets. The following services are defined:

get_all_rows: Retrieves all rows from the Google Sheet.
initialize_gspread: Initializes the connection to the Google Sheets API.
You can configure the Google Sheets ID and worksheet names directly in the service layer of the project.

Screenshots
Main List Page

Add Entry Form

Edit Entry Form

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new pull request.
