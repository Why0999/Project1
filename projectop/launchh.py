from os import truncate
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

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
