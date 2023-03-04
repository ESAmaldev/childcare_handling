#Child care data from England
The project is displaying the data collected from child welfare centres across England during the period of 2018-19. 

##Installation
command to install new python version---> pyenv install 3.7.0
command to set python env version ------> pyenv local 3.7.0

to install flask -----------------------> pip install flask
to upgrade flask -----------------------> pip install --upgrade pip

command to create virtual environment --> python3 -m venv .venv
command to activate virtual environment > source .venv/bin/activate

command to export the app --------------> export FLASK_APP=webApp.py
command to set environment to developer-> export FLASK_ENV=development

command to start the server ------------> python3 -m flask run -host 0.0.0.0

##Usage
The /index.html to open the home page where users will have option to select a region and 
view data from that region. One the right there is an option for users to enter new data. 
On top of the page there is a home button which will allow users to redirect to home page.
Click on the inspection number in location data to view the inspection data. To upload new 
data , place csv file in home directory, name it childcare_data.csv and Run setup_db.py to
upload data into the database.
