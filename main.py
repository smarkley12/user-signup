from flask import Flask, render_template, request, redirect
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_info():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_name_error = ''
    password_verify_error = ''
    password_not_valid_error = ''
    email_error = ''
    test = ' '

    if len(username) > 20 or len(username) < 3:
        user_name_error = "That's not a valid username."
    elif test in username == True:
        user_name_error = "That's not a valid username."


    if len(password) > 20 or len(password) < 3:
        password_not_valid_error = "That's not a valid password."
        password = ''
    elif ' ' in password == True:
        password_not_valid_error = "That's not a valid password."
        password = ''

    if password != verify:
        password_verify_error = "Passwords don't match"
        verify = ''

    if '@' not in email:
        email_error = "That's not a valid email."
        
    if '.' not in email:
        email_error = "That's not a valid email."

    if len(email) > 20 or len(email) < 3:
        email_error = "That's not a valid email."
    if email == '':
        email_error = ''
    
    
    
    if not user_name_error and not password_not_valid_error and not \
    password_verify_error and not email_error:
        return redirect('/valid?username={0}'.format(username))
    else: 
        return render_template('index.html', 
            password_not_valid_error=password_not_valid_error,
            password_verify_error=password_verify_error, 
            user_name_error=user_name_error, 
            email_error=email_error,
            username=username, email=email)


@app.route('/valid', methods=['POST', 'GET'])
def valid():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()