## IEOR E4501 - Squirrel Tracker Project

### Project Description
This project is for tracking squirrels in Central Park. It can import the 2018 Central Park Squirrel Census data and allows you to add, update, and view squirrel data.

This project is `Django` based.

### reference code to runserver
git clone xxxx
cd E4501-SquirrelProject/

python3 -m venv env
source env/bin/activate		

pip install -r requirements.txt 
python manage.py makemigrations
python manage.py migrate
python manage.py import_squirrel_data file.csv

pwd
sudo /home/xxxxxx/E4501-SquirrelProject/env/bin/python manage.py runserver 0.0.0.0:80

### Group Name and Section
Mudi & Kahn, section 1

### UNIs
UNIs: [ml4538, ay2514]
