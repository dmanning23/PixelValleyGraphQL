import os
from mongoengine import *
#from keys import mongoUri

mongoUri = os.getenv("mongoUri")
#connect(host=mongoUri, db="pixelValley") #connect for mongoengine
