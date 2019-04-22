from flask import Flask, render_template, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

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
        password_not_valid_error = "That's not a valid username."
        password = ''
    elif ' ' in password == True:
        password_not_valid_error = "That's not a valid username."
        password = ''

    if password != verify:
        password_verify_error = "Passwords don't match"
        verify = ''

    if len(email) > 20 or len(email) < 3:
        email_error = "That's not a valid email."
    elif '@' in username == True:
        email_error = "That's not a valid email."
    elif '.' in username == True:
        email_error = "That's not a valid email."
    
    
    if not user_name_error and not password_not_valid_error and not \
    password_verify_error and not email_error:
        return redirect('/valid')
    else:
        template = jinja_env.get_template('index.html') 
        return template.render (password_not_valid_error=password_not_valid_error,
                password_verify_error=password_verify_error, 
                user_name_error=user_name_error, email_error=email_error,
                username=username, email=email)


@app.route('/valid')
def valid():
    username = request.form['username']
    template = jinja_env.get_template('welcome')
    return template.render(username=username)

app.run()