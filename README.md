# Ambulance and Patient Tracking

### Basic Information
This is a Django based web application used to upload the
exact co-ordinates of an accident location, where driver can get
this location and will reach the spot using the built-in maps in this website.

## Instructions
  1. Open Command prompt or Terminal
  2. Download the project folder using command https://github.com/kalerukoushik/ambulance_tracking.git 
  (this won't work in windows unless you download Git - https://git-scm.com/downloads) or just download the zip file.
  3. ```cd ambulance_tracking```
  (Make sure you installed Python)
  4. Its better to use a Virtual environment. Install it by using ```pip install virtualenvwrapper-win```
  5. After that, type the command ```mkvirtualenv <name>``` to create a virtual environment.
  6. Then activate the environment by ```workon <name>```.
  7. Now it's time to install all the modules needed to run this project.
  8. First install Django using ```pip install django```.
  8. Type ```pip install -r requirements.txt```.
  
## Database setup
  1. This is it. But before running the server we should do something with the database setup.
  2. Download and install PostgreSQL - ```https://www.postgresql.org/download/``` and pdAdmin tool ```https://www.pgadmin.org/download/``` which supports your OS.
  3. While installing PostgreSQL, create a password which will be asked. Open PgAdmin and type the password which you just created while installing PostgreSQL and create the database amb_track.
  4. Now open the command prompt by activating the environment setup.
  5. Type following commands to migrate the database.
    i. ```python manage.py makemigrations```
    ii. ```python manage.py migrate```
## Run server
  1. Now, you can run the project by typing ```python manage.py runserver```.
  2. Open the webpage by using typing ```localhost:8000/home``` in your favourite browser.
  3. This is the user's home page.
  4. Open ```localhost:8000/driver/login``` for driver webpages.
  
  ### Admin setup
  1. To open admin type ```localhost:8000/admin```
  2. Django Administration page will be displayed which asks for username and password which you don't have at present.
  3. To create it, open cmd in the virtual environment and type ```python manage.py createsuperuser```.
  4. Type in the username, email, and password to create the admin account.
  5. Now open the admin page and type in those creddentials those which you just created.
  6. Tada, Thats it, The project is now up and running completely.
