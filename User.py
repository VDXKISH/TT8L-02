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


login_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        .login {
            border: 1px solid black;
            width: 400px;
            height: 500px;
            background: url('your-background-image-url.jpg');
            color: rgb(103, 245, 207);
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.75);
            background-size: cover;
            background-position: center;
            overflow: hidden;
            margin: 50px auto; 
            padding: 20px;
        }

        .header {
            text-align: center;
        }

        form {
            display: block;
            box-sizing: border-box;
            padding: 40px;
            width: 100%;
            height: 100%;
            backdrop-filter: brightness(40%);
            flex-direction: column;
            display: flex;
            gap: 15px; 
        }

        h1 {
            font-weight: normal;
            font-size: 24px;
            text-shadow: 0px 0px 2px rgba(0,0,0,0.5);
            margin-bottom: 20px; /* Adjusted margin */
            text-align: center;
        }

        label {
            color: rgba(255, 255, 255, 0.8);
            text-transform: uppercase;
            font-size: 10px;
            letter-spacing: 2px;
            padding-left: 10px;
        }

        input {
            background: rgba(128, 251, 189, 0.3);
            height: 40px;
            line-height: 40px;
            border-radius: 20px;
            padding: 0px 20px;
            border: none;
            margin-bottom: 20px;
            color: white;
        }

        button {
            background: rgba(45, 126, 231, 1);
            height: 40px;
            line-height: 40px;
            border-radius: 40px;
            border: none;
            margin: 10px 0px;
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
            color: white;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        button:hover {
            background: rgba(45, 126, 231, 0.8);
        }

        .header h1 {
            margin-bottom: 20px; 
        }

        .SIGN_UP-link {
            text-align: center;
            margin-top: 20px;
        }

        .SIGN_UP-link a {
            color: white;
            text-decoration: none;
            font-size: 14px;
            transition: color 0.3s ease;
        }

        .SIGN_UP-link a:hover {
            color: rgba(255, 255, 255, 0.8);
        }
    </style>
</head>
<body>
    <div class="login">
        <div class="header">
            <h1>WELCOME TO LIGHTNING BUS</h1>
        </div>
        <form method="POST">
            <h1>Log In</h1>
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Enter your username" required>
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Enter your password" required>
            <button type="submit">Submit</button>
            <div class="SIGN_UP-link">
                <a href="{{ url_for('SIGN_UP') }}">Don't have an account? Sign Up</a>
            </div>
        </form>
    </div>
</body>
</html>
'''


SIGN_UP_html = '''
<!DOCTYPE html>
<html lang="en"> 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .sign-up {
            background-color: #515151;
            border: 1px solid black;
            width: 400px;
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.75);
            overflow: hidden;
            color: white;
        }

        form {
            padding: 40px;
        }

        h1 {
            font-weight: normal;
            font-size: 24px;
            margin-bottom: 40px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            color: rgba(255, 255, 255, 0.9);
            font-size: 12px;
            letter-spacing: 1px;
        }

        input[type="email"],
        input[type="text"],
        input[type="password"] {
            background: rgba(6, 216, 181, 0.3);
            height: 40px;
            line-height: 40px;
            border-radius: 20px;
            padding: 0px 20px;
            border: none;
            width: 100%;
            color: white;
        }

        button {
            background: rgba(45, 126, 231);
            height: 40px;
            line-height: 40px;
            border-radius: 40px;
            border: none;
            margin-top: 20px;
            width: 100%;
            color: white;
            cursor: pointer;
        }

        button:hover,
        button:focus {
            background: rgba(45, 126, 231, 0.8);
        }

        input:focus,
        input:hover {
            background: rgba(6, 216, 181, 0.5);
        }
    </style>
</head>
<body>
<div class="sign-up">
    <form method="POST"> 
        <h1>Sign Up</h1>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Your email" required>
        <label for="fullname">Full Name</label>
        <input type="text" id="fullname" name="fullname" placeholder="Your full name" required>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" placeholder="Your username" required>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" placeholder="Your password" required>
        <button type="submit">Submit</button>
        <div class="SIGN_UP-link">
            <a href="{{ url_for('login') }}">Back to Login Page</a>
        </div>
    </form>
</div>
</body>
</html>
'''

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
