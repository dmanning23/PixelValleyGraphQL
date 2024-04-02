import os
from flask import Flask
from flask_cors import CORS, cross_origin
from mongoengine import *

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mongoUri = os.getenv("mongoUri")
connect(host=mongoUri, db="pixelValley") #connect for mongoengine

@app.route('/')
@cross_origin()
def hello():
    return 'My First API !!'