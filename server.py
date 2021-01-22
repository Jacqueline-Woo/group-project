from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import csv
import os
import time
from flask_login import current_user
from flask_login import login_required, LoginManager, login_user
from datetime import datetime

app = Flask(__name__)


picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder


# HTML form
@app.route('/login')
def login():
    log_in = os.path.join(app.config['UPLOAD_FOLDER'],'log_in.png')
    return render_template("login.html", log_in = log_in)



@app.route('/login', methods=["POST"])
def users_login_email_password():
    userdata = dict(request.form)
    email = userdata["email"]
    password = userdata["password"]
    if( len(password)<10):
        return render_template("login.html", status="Invalid password, please enter a password with a minimum of 10 characters.")
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                if( row[3].strip() == email.strip() and row[4].strip() == password.strip() ):
                    return render_template("submit.html", status="User found!",users = users)
                # This is for if the email is right but password is wrong.
                elif ( row[3].strip() == email.strip() and not row[4].strip() == password.strip() ):
                    return render_template("login.html",status = "Incorrect password. Please try again.")
            else:
                first_line = False

    if not ( row[3].strip() == email.strip() and row[4].strip() == password.strip() ):
            return render_template("new_user.html",status = "Don't have account? Register now!")

@app.route('/button')
def button():
    return render_template("new_user.html")

@app.route('/')
def hello_world():
    homepic = os.path.join(app.config['UPLOAD_FOLDER'],'homepic.png')
    return render_template("index.html", homepic = homepic)

# HTML page?
@app.route('/about')
def about_us():
    #pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'pic2.gif')
    aboutus2 = os.path.join(app.config['UPLOAD_FOLDER'],'aboutus2.png')
    lol = os.path.join(app.config['UPLOAD_FOLDER'],'lol.gif')
    pic5 = os.path.join(app.config['UPLOAD_FOLDER'],'pic5.gif')
    pic6 = os.path.join(app.config['UPLOAD_FOLDER'],'pic6.gif')
    return render_template("about_us.html", user_image5 = pic5, user_image6 = pic6, lol_image = lol, aboutus_image2 = aboutus2)

@app.route('/hello/<uname>')
def say_hello(uname):
    return 'Hello ' + uname

# Read from a CSV
@app.route('/users')
def return_users():
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                users.append({
                "fname": row[0],
                "lname": row[1],
                "city": row[2]
                })
            else:
                first_line = False
    return render_template("index.html", users=users)

# HTML form
@app.route('/newUser')
def new_user():
    reg = os.path.join(app.config['UPLOAD_FOLDER'],'reg.gif')
    return render_template("new_user.html", reg_image = reg)

# Write to a CSV file
@app.route('/newUser', methods=["GET", "POST"])
def submit_form():
    if request.method == "GET":
        return redirect(url_for('newUser'))
    elif request.method == "POST":
        userdata = dict(request.form)
        fname = userdata["fname"]
        lname = userdata["lname"]
        city = userdata["city"]
        email = userdata["email"]
        password = userdata["password"]
        confirmpassword = userdata["confirmpassword"]
        if( len(fname) < 1 or len(lname) < 1 or len(city) < 1 or len(email) < 1 or len(password) < 10  or len(confirmpassword) < 10 ):
            return render_template("new_user.html", status='Please resubmit with valid information. Make sure your password has a minimum of 10 characters!')
        else:
            with open('data/users.csv', mode='a', newline='') as file:
                data = csv.writer(file)
                data.writerow([fname, lname, city, email, password, confirmpassword])
            # return render_template("new_user.html", status='You have successfully created an account!') 
            return render_template("submit.html", status='You have successfully created an account!')

# HTML form
@app.route('/getUser')
def get_user():
    return render_template("get_user.html")

@app.route('/getUser', methods=["POST"])
def return_users_by_city():
    userdata = dict(request.form)
    post = userdata["post"]
    if( len(post) < 1 ):
        return render_template("get_user.html", status="Invalid Post")
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                if( row[2].strip() == city.strip() ):
                    users.append({
                    "fname": row[0],
                    "lname": row[1]
                    })
            else:
                first_line = False
    if( len(users) == 0 ):
        status = "No Users Found for specified city."
    else:
        status = "Users found!"
    return render_template("get_user.html", status=status, users=users)

# HTML form - Submit page
@app.route('/submit')
def submit():
    post_image = os.path.join(app.config['UPLOAD_FOLDER'],'post.gif')
    return render_template("submit.html", post_image = post_image)

@app.route('/submit', methods=["GET", "POST"])
def submit_post():
    if request.method == "GET":
        return redirect(url_for('submit'))
    elif request.method == "POST":
        submission = dict(request.form)
        post = submission["post"]
        #time = submission["time"]
        if( len(post) < 1 ):
            return render_template("submit.html", status='Submission was blank. Please try again.')
        else:
            #dateTimeObj = datetime.now()
            #timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            #time = timestampStr
            with open('data/posts.csv', mode='a', newline='') as file:
                data = csv.writer(file, delimiter=',')
                data.writerow([post])
            return render_template("submit.html", status='Post submitted!', post=post)

# taken from https://kellylougheed.medium.com/make-a-flask-app-with-a-csv-as-a-flat-file-database-373632a2fba4
#@app.route("/feed")
#def display_post():
#  with open('.data/posts.csv') as file:
#    data = csv.reader(file)
#    first_line = True
#    posts = []
#    for row in data:
#      if not first_line:
#        posts.append({
#          "post": row[0]
#        })
#      else:
#        first_line = False
#  return render_template("index.html", post=post)

@app.route('/posts')
def return_posts():
    with open('data/posts.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        posts = []
        for row in data:
            if not first_line:
                posts.append({
                "post": row[0], 
                #"time": row[1]
                })
                #print(f'\tPOST: {row[0]}')
            else:
                first_line = False
    return render_template("posts.html", posts=posts)

#@app.route('/seeposts')
#def see_posts():
#    return redirect(url_for('/posts'))

        #if( len(post) == 0 ):
            #return render_template("feed.html", status='Submission was blank. Please try again.')
        #else:
            #return render_template("feed.html", status='Post submitted!', post=post)

# the following is part of feed
#def return_posts():
    #if( len(post) == 0 ):
        #status = "You submitted a blank post. Please try again."
    #else:
        #status = "Post submitted!"
        #return render_template("feed.html", status=status, post=post)