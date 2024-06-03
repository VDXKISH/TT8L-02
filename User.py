from flask import Flask, request, render_template_string, redirect, url_for
import json


app = Flask(__name__)

USERS_FILE = 'users.json'

def load_users():
    try:
        with open(USERS_FILE, 'r') as file: # r is read mode
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_users(users):
    with open(USERS_FILE, 'w') as file: # w is write mode
        json.dump(users, file)


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        if username in users and users[username]['password'] == password: 
            return "Logged in successfully!"
        else:
            return "Invalid username or password, please try again."
    return render_template_string(login_html)

@app.route('/SIGN_UP', methods=['GET', 'POST'])
def SIGN_UP():
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        

        users = load_users()
        users[username] = {'email': email, 'fullname': fullname, 'password': password}
        save_users(users)


        return redirect(url_for('login'))
    return render_template_string(SIGN_UP_html)

if __name__ == '__main__':
    app.run(debug=True)
