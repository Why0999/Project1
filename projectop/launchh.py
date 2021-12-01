from os import truncate
from flask import Flask, render_template, url_for, flash, redirect

from flask import jsonify
from flask import request
from flask import make_response
import pymysql.cursors 
from flask_cors import CORS,cross_origin
import string
import random
from datetime import *

app = Flask(__name__)

config = {
  'ORIGINS': [
    'http://localhost:3000',  # React
    'http://127.0.0.1:3000',  # React
  ],
}

CORS(app,resources={ r'/*': {'origins': config['ORIGINS']}}, supports_credentials=True)
 
conn = pymysql.connect(host='localhost',
                       user='ronal',
                       password='password',
                       db='Vac',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

@app.route("/")
def home():
    return render_template('home.html') #Connect to home.html

@app.route("/about") #URL extension
def about():
    return render_template('about.html', title='About') #Connect to about.html

@app.route("/1") #URL extension
def page2():
    return "Another Page" 

if __name__ == '__main__':
    app.run(debug=True)
## Can do -"python launchh.py" in CMD instead of flask launch.
## Note: Switch CMD to project folder.
