from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def hello_world():
    return render_template("index.html")

# HTML page?
@app.route('/about')
def about_us():
   return render_template("about_us.html")

# HTML page?
@app.route('/profile')
def profile():
   return render_template("profile.html")

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
                "city": row[2],
                "email": row[3],
                "password": row[4],
                "confirmpassword": row[5]
                })
            else:
                first_line = False
    return render_template("index.html", users=users)

# HTML form
@app.route('/newUser')
def new_user():
    return render_template("new_user.html")

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
        if( len(fname) < 1 or len(lname) < 1 or len(city) < 1 or len(email) < 1 or len(password) < 1  or len(confirmpassword) < 1 ):
            return render_template("new_user.html", status='Please resubmit with valid information.')
        else:
            with open('data/users.csv', mode='a', newline='') as file:
                data = csv.writer(file)
                data.writerow([fname, lname, city, email, password, confirmpassword])
            return render_template("feed.html", status='You have successfully created an account!') 
            

# HTML form
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def users_login_email_password():
    userdata = dict(request.form)
    email = userdata["email"]
    password = userdata["password"]
    #if( len(password)<10):
        #return render_template("login.html", status="Invalid email and password, please enter again.")
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                if( row[3].strip() == email.strip() and row[4].strip() == password.strip() ):
                    return render_template("submit.html", status="Users found!",users = users)
            else:
                first_line = False
    if (row[4].strip() == password.strip() ):
        if not (row[3].strip() == email.strip()):
            return render_template("login.html", status="Please login with your sbu mail")


@app.route('/submit')
def feed():
    return render_template("submit.html")

@app.route('/submit', methods=["GET", "POST"])
def submit_post():
    if request.method == "GET":
        return redirect(url_for('submit'))
    elif request.method == "POST":
        submission = dict(request.form)
        post = submission["post"]
        if( len(post) < 1 ):
            return render_template("submit.html", status='Submission was blank. Please try again.')
        else:
            with open('data/posts.csv', mode='a', newline='') as file:
                data = csv.writer(file)
                data.writerow([post])
            return render_template("submit.html", status='Post submitted!', post =post)

@app.route('/button')
def button():
    return render_template("new_user.html")

@app.route('/posts')
def return_posts():
    with open('data/posts.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        posts = []
        for row in data:
            if not first_line:
                posts.append({
                "post": row[0]
                })
                #print(f'\tPOST: {row[0]}')
            else:
                first_line = False
    return render_template("posts.html", posts=posts)