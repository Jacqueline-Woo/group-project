from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return 'This site was developed by Arpita'

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
        if( len(fname) < 1 or len(lname) < 1 or len(city) < 1 ):
            return render_template("new_user.html", status='Please resubmit with valid information.')
        else:
            with open('data/users.csv', mode='a', newline='') as file:
                data = csv.writer(file)
                data.writerow([fname, lname, city])
            return render_template("new_user.html", status='User added!')

# HTML form
@app.route('/getUser')
def get_user():
    return render_template("get_user.html")

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
    return render_template("get_user.html", status=status, users=users)

# HTML form - Feed page (submit and display posts)
@app.route('/feed')
def feed():
    return render_template("feed.html")

@app.route('/feed', methods=["GET", "POST"])
def submit_post():
    if request.method == "GET":
        return redirect(url_for('feed'))
    elif request.method == "POST":
        submission = dict(request.form)
        post = submission["post"]
        if( len(post) < 1 ):
            return render_template("feed.html", status='Submission was blank. Please try again.')
        else:
            with open('data/posts.csv', mode='a', newline='') as file:
                data = csv.writer(file)
                data.writerow([post])
            return render_template("feed.html", status='Post submitted!')

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