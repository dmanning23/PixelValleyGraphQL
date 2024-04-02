from flask import Flask
from flask_cors import CORS
from keys import mongoUri
from mongoengine import *

app = Flask(__name__)
CORS(app)

connect(host=mongoUri, db="pixelValley") #connect for mongoengine

@app.route('/')
def hello():
    return 'My First API !!'