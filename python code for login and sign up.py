from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "admin" and password == "password": 
            return "Logged in successfully!"
        else:
            return "Invalid username or password, please try again."
    return render_template_string(login_html, login_css=login_css)

@app.route('/SIGN_UP', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        
        return "Sign up successful!"
    return render_template_string(SIGN_UP_html, SIGN_UP_css=SIGN_UP_css)

if __name__ == '__main__':
    app.run(debug=True)