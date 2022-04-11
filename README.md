# Sites Travel


## Backend server
### Installation of the virtual enviroment(For example env)
cd backend
python3 -m venv <venv>
source <venv>/bin/activate
pip install -r requirements.txt
python manage.py runserver


#### Dump initial data
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > db.json

#### Load intitial fixtures
python manage.py loaddata db.json