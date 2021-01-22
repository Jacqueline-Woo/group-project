from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import csv
import os
from flask_login import current_user
from flask_login import login_required, LoginManager, login_user

app = Flask(__name__)




picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder



@app.route('/')
def hello_world():
    homepic = os.path.join(app.config['UPLOAD_FOLDER'],'homepic.png')
    return render_template("index.html", homepic = homepic)
    #return render_template("index.html")

<<<<<<< HEAD
<<<<<<< HEAD
# HTML page?
@app.route('/about')
def about_us():
   return render_template("about_us.html")

# HTML page?
@app.route('/profile')
def profile():
   return render_template("profile.html")
=======
@app.route('/about')
def about():
    return 'This site was developed by Arpita'
>>>>>>> 9d0b1be352caa575c8f6d9fb67109cdf49fac70c
=======
# HTML page?
@app.route('/about')
def about_us():
    #pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'pic2.gif')
    aboutus2 = os.path.join(app.config['UPLOAD_FOLDER'],'aboutus2.png')
    lol = os.path.join(app.config['UPLOAD_FOLDER'],'lol.gif')
    pic5 = os.path.join(app.config['UPLOAD_FOLDER'],'pic5.gif')
    pic6 = os.path.join(app.config['UPLOAD_FOLDER'],'pic6.gif')
    return render_template("about_us.html", user_image5 = pic5, user_image6 = pic6, lol_image = lol, aboutus_image2 = aboutus2)


# HTML page?
#@app.route('/profile')
#@login_required
#def profile():
  #image_file = url_for('static', filename = 'pics/' + current_user.image_file)
  #pic3 = os.path.join(app.config['UPLOAD_FOLDER'],'pic3.gif')
  #pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'pic2.gif')
 # return render_template("profile.html")


  #return render_template("profile.html", user_image3 = pic3,  user_image2 = pic2)
  #return render_template("profile.html",title = 'Profile',image_file=image_file) 





#@app.route('/profile')
#def profile(username):
 #   user = User.query.filter_by(username=username).first_or_404()
 # posts = [
  #      {'author': user, 'body': 'Test post #1'},
   #     {'author': user, 'body': 'Test post #2'}
    #]
    #return render_template('profile.html', user=user, posts=posts)


>>>>>>> c0168c0057894fecd7d50335f302b897cd7ed806

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
<<<<<<< HEAD
                "city": row[2],
                "email": row[3],
                "password": row[4],
                "confirmpassword": row[5]
=======
                "city": row[2]
>>>>>>> 9d0b1be352caa575c8f6d9fb67109cdf49fac70c
                })
            else:
                first_line = False
    return render_template("index.html", users=users)


# Read from a CSV
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
            else:
                first_line = False
    return render_template("posts.html", posts=posts)


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
        if( len(post) < 1 ):
            return render_template("submit.html", status='Submission was blank. Please try again.')
        else:
            with open('data/posts.csv', mode='a', newline='') as file:
                data = csv.writer(file, delimiter=',')
                data.writerow([post])
            #dateTimeObj = datetime.now()
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
            else:
                first_line = False

    if not ( row[3].strip() == email.strip() and row[4].strip() == password.strip() ):
            return render_template("new_user.html",status = "Don't have account? Register now!")


# HTML form
#@app.route('/newUser')
#def new_user():
 #   reg = os.path.join(app.config['UPLOAD_FOLDER'],'reg.gif')
  #  return render_template("new_user.html", reg_image = reg)

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
<<<<<<< HEAD
<<<<<<< HEAD
        email = userdata["email"]
        password = userdata["password"]
        confirmpassword = userdata["confirmpassword"]
        if( len(fname) < 1 or len(lname) < 1 or len(city) < 1 or len(email) < 1 or len(password) < 1  or len(confirmpassword) < 1 ):
=======
        if( len(fname) < 1 or len(lname) < 1 or len(city) < 1 ):
>>>>>>> 9d0b1be352caa575c8f6d9fb67109cdf49fac70c
            return render_template("new_user.html", status='Please resubmit with valid information.')
        else:
            with open('data/users.csv', mode='a', newline='') as file:
                data = csv.writer(file)
<<<<<<< HEAD
                data.writerow([fname, lname, city, email, password, confirmpassword])
            return render_template("new_user.html", status='You have successfully created an account!') 
            
=======
                data.writerow([fname, lname, city])
            return render_template("new_user.html", status='User added!')
>>>>>>> 9d0b1be352caa575c8f6d9fb67109cdf49fac70c
=======
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
>>>>>>> c0168c0057894fecd7d50335f302b897cd7ed806


<<<<<<< HEAD
@app.route('/getUser', methods=["POST"])
def return_users_by_city():
    userdata = dict(request.form)
    city = userdata["city"]
    if( len(city) < 1 ):
        return render_template("get_user.html", status="Invalid City")
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
<<<<<<< HEAD
    return render_template("get_user.html", status=status, users=users)
=======
    return render_template("get_user.html", status=status, users=users)
>>>>>>> 9d0b1be352caa575c8f6d9fb67109cdf49fac70c
=======
@app.route('/button')
def button():
    return render_template("new_user.html")
>>>>>>> c0168c0057894fecd7d50335f302b897cd7ed806
