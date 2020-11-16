# TOL-Trainer
Note: This project is originally hosted [here](https://github.com/IOLTaiwan/TOL_Trainer). It points to my old GitHub account which is now out of use. The setup instructions is adapted from the work of [@puerdon](https://github.com/puerdon).
##Summary
TOL-Trainer is a Flask application for creating, storing and hosting competitive linguistics questions. Users can log in, view and solve the assigned questions. Administrators can view and grade each response, as well as add and modify questions. User and question information is stored via SQLite.

## Setup
1. Activate python venv (python > 3.6)

2. Install dependencies
```
$ pip install -r requirements.txt
```

3. Set up environmental variables（Can be saved as .env file）
```
SECRET_KEY=''
SQLALCHEMY_DBURI='sqlite:///site.db'
FLASK_APP='run.py'
EMAIL_USER='(Email to send from)'
EMAIL_PASS='(Email password'
```

4. Read environmental variables
```
$ source <filename.env>
```

### For development only

5. Launch flask
```
$ flask run
```

### For deployment only

The project is deployed using nginx and uwsgi

#### uwsgi.ini

```
$ uwsgi --ini uwsgi.ini
```


#### Restart nginx
```
$ sudo systemctl restart nginx
```
---
Author: Kevin Chen ([@kchendv](https://github.com/kchendv))