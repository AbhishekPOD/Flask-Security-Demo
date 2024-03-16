# Flask-Security-Demo

A simple setup of a flask application to demonstrate token based authentication and role based authorization

### Steps to run the application:

1. Create a virtual environment and activate it using the below comands.

```
python -m venv .env
```

```
source .env/Scripts/activate
```

2. Install the dependencies

```
pip install flask flask-sqlalchemy flask-security-too bcrypt==4.0.1

OR

pip install -r req.txt
```

3. Run the `add_data.py` file using the below command to create and ingest data to the database file.

```
python add_data.py
```

4. Run the app using the below command.

```
python main.py
```