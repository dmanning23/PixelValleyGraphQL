from flask import Flask
from flask_cors import CORS
#from keys import mongoUri
from mongoengine import *
import os

app = Flask(__name__)
CORS(app)

mongoUri = os.getenv("mongoUri")
connect(host=mongoUri, db="pixelValley") #connect for mongoengine

@app.route('/')
def hello():
    return 'My First API !!'