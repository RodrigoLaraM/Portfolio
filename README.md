# Welcome to the Dancing Ducks' Portfolio Site!

## Quickstart
Clone the `main` branch of the repository into your own local repository. 

_Make sure you have python3 and pip installed!_

Create and activate virtual environment using `virtualenv`.
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!
```bash
$ pip install -r requirements.txt
```
Run the Flask server:
```bash
$ flask run
```
Now you can access the site locally at localhost:5000 or 127.0.0.1:5000!

## Configuration / environment variables
To run the flask server under developer mode, enter this into bash before running it:
```bash
$ export FLASK_ENV=development
$ flask run
```
**Developer mode** restarts the server automatically every time changes are made! Otherwise, you would have to type `flask run` every time you make a change.
Alternatively, we encourage creating a `.env` file (literally just named `.env`) that holds all your flask configuration so you do not have to type it in bash all the time:
```
URL=localhost:5000
FLASK_ENV=development
```

## Directory structure
All static files, including stylesheets and image files are stored in the `static` folder. These are things that do not get dynamically updated with Python and Flask!
All page templates are stored in the `templates` folder. Flask looks for HTML/Jinja templates here and dynamically displays them.
