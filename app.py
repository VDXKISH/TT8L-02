from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

posts = [{
    'name': 'is me',
    'date': '10/12'
}]

@app.route("/")
def home():
     return  render_template('index.html', posts = posts)

@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "POST":
        user = request.form('toState'), request.form('state'), 
        if user == 'Selangor''Johor Baharu':
            return  render_template('index.html',posts = posts)
        
    else:
        return render_template("index.html")