from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

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
<<<<<<< HEAD
    return render_template("get_user.html", status=status, users=users)
=======
    return render_template("get_user.html", status=status, users=users)
>>>>>>> 9d0b1be352caa575c8f6d9fb67109cdf49fac70c
