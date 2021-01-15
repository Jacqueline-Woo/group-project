# python-flask-intro
Introductory Material for Learning Python Flask

## Requirements
Python 3, pip

## Setup

Using the command line, first ```cd``` into the project folder.

First, create the virtual environment (```venv```). This only needs to be done the first time you run the project.

```
python -m venv venv
py -3 -m venv venv (Windows)
```

Next, we will activate the virtual enviroment

```
. venv/bin/activate
venv\Scripts\activate (Windows)
```

Now, let's install needed libraries to the virtual environment. This only needs to be done when the ```venv``` is first created or when ```requirements.txt``` is updated.

```
pip install -r requirements.txt
```

Finally, it is time to run our project.

```
export FLASK_APP=server.py
set FLASK_APP=server.py (Windows)
$env:FLASK_APP = "server.py" (Windows Powershell)
flask run
```

While developing, it may help to auto-refresh without needing to stop Flask from running. You can do this by enabling development mode
```
export FLASK_ENV=development
set FLASK_ENV=development (Windows)
```
