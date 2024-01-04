# KAMI Airlines API Overview

This project is a RESTful API developed using Django Rest Framework for KAMI Airlines.


## Installation and Setup

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/

Accessing the API
Visit http://127.0.0.1:8000/api/airplane to view or modify the airplanes.

An API documentation for this project is included in "**KAMI Airlines API Collection.json**" which you can directly import in Postman to test the functionality

### Testing
Coverage testing report is also included as HTML in **htmlcov** folder

To run coverage test

```bash
coverage run --source='airplane' manage.py test
```