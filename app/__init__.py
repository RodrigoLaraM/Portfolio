import os
import re
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime as dt

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
user=os.getenv("MYSQL_USER"),
password=os.getenv("MYSQL_PASSWORD"),
host=os.getenv("MYSQL_HOST"),
port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=dt.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# dictionary of all information about fellows. Will be passed in a render_template call and used in a jinja template.
# "name": {
#         "first": "",
#         "last": "",
#         "about": "",
#         "image": "",
#         "socials": [
#             {
#                 "name": "",
#                 "link": ""
#             }
#         ],
#         "education": [
#             {
#                 "institution": "",
#                 "grad_date": "",
#                 "courses": "",
#             }
#         ],
#         "experience": [
#             {
#                 "position": "",
#                 "company": "",
#                 "dates": "",
#                 "desc": ""
#             }
#         ],
#         "resume": "",
#         "hobbies": [
#             {
#                 "name": "",
#                 "image": "",
#                 "desc": ""
#             }
            
#         ]
#     }
fellows = {
    "rodrigo": {
        "first": "Rodrigo",
        "last": "Lara",
        "github": "https://github.com/RodrigoLaraM",
        "linkedin": "https://www.linkedin.com/in/rodrigolaram/",
        "resume": "",
        "about": "Hi! I'm Rodrigo Lara. A rising senior at Michigan State University majoring in Data Science",
        "image": "/static/img/lara-mlh.jpg",
        "education": [
            {
                "institution": "Michigan State University",
                "grad_date": "December 2023",
                "courses": "Data Science Major & Business Minor"
            }
        ],
        "experience": [
            {
                "position": "Teaching Assistant",
                "company": "Michigan State University",
                "dates": "January 2022 - May 2022",
                "desc": "I taught an introductory Python programming and algorithmic thinking course to 35 students.",
            },
          
        ],
        "hobbies": [
            {
                "name": "Reading",
                "image": "/static/img/books.jpeg",
                "desc": "I'm mainly interested finance, geopolitics and phylosophy"
            },
            {
                "name": "Music Production",
                "image": "/static/img/ableton.png",
                "desc": "On free times I write electronic music",
            }
        ],
        "locations": [
            {
                "location": "Paris, FR",
                "coordinates": [48.8566, 2.3522],
                "desc": "Beuatiful Eiffel Tower"
            },
            {
                "location": "Barcelona, SP",
                "coordinates": [41.3874, 2.1686],
                "desc": "Best 'Jamon Serrano' I've ever had"
            },
            {
                "location": "Reynosa, MX",
                "coordinates": [26.0508, -98.2979],
                "desc": "The city I was raised in"
            },
            {
                "location": "Chicago, IL",
                "coordinates": [41.8781, -87.6298],
                "desc": "I went once to see my favorite artist, Flume, at Lollapalooza"
            },
            {
                "location": "Cancun. MX",
                "coordinates": [21.1619, -86.8515],
                "desc": "Some of the most beautiful beaches in Mexico."
            }
        ],
        "projects": [
            {
                "name": "NAFTA Obesity Epidemic",
                "type": "Data Analysis",
                "language": "Python",
                "desc": "The question of this investigation is if there is some truth behind the numerous accusations that the NAFTA has flooded Mexico with obesity and malnutrition. By using different analysis methods and techniques I was able to formulate a conclusion to this question.",
                "link": "/static/projects/CMSE201_FinalProject.html",
                "repo": "https://github.com/RodrigoLaraM/NAFTA-Obesity-Analysis-Project.git",
                "image": "/static/img/NAFTA_img.png"
            },
            {
                "name": "College Football Analysis",
                "type": "Data Analysis",
                "language": "R",
                "desc": "Is there any correlation between specific football team performance and victories on college level football? On this research paper by using numerous statistical methods and analysis in R different result were gathered on this matter",
                "link": "/static/projects/Project_Writeup.html",
                "repo": "https://github.com/RodrigoLaraM/College_Football_Analysis_Project.git",
                "image": "/static/img/Football.png"                
            }
        ]
    }
}

load_dotenv()
app = Flask(__name__)

# home page route
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), fellows=fellows)

# fellow's pages route
# input the dictionary of a fellow's information using fellows[name]
@app.route('/fellow/<name>')
def show_profile(name):
    return render_template('profile.html', title=fellows[name]['first']+' '+fellows[name]['last'], fellow=fellows[name], url=os.getenv("URL"))

@app.route('/hobbies')
def show_hobby():
    return render_template('hobbies.html', title="Hobbies", fellows=fellows, url=os.getenv("URL"))

@app.route('/projects')
def show_projects():
    return render_template('projects.html', title="Projects", fellows=fellows, url=os.getenv("URL"))

@app.route('/map')
def show_map():
    return render_template('map.html', title="Travel", fellows=fellows, url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
    