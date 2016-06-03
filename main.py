from flask import Flask, render_template,request, flash,  url_for, redirect, session
from content  import contentManagement
from functools import wraps
from flask_mail import Message, Mail
import smtplib


app=Flask(__name__)
app.secret_key = '15%&*^&^GJHYTDT24623/*@!@#G@JH$%+9'
levelsContent, exercicesContent, exercicesWarmingUp=contentManagement()

app.config.update(
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 587,
    MAIL_USE_SSL = False,
    MAIL_USE_TLS =True,
    MAIL_USERNAME = "deliverymessage0@gmail.com",
    MAIL_PASSWORD = "saq123ew"
)
mail = Mail(app)


@app.route("/")
def index():
    try:
        return render_template("presentacion.html")
    except Exception as e:
        return "error in the method index " +str(e)


@app.route("/logout/")
def logout():
    try:
        session.pop('username', None)
        session.pop('password', None)
        flash("Te esperamos pronto")
        return render_template("presentacion.html")
    except Exception as e:
        return "error in the method logout " +str(e)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            ##I use args when I dont know how many parameters I going to pass to the function
            ## *args is a tuple of argumets
            ## **args is a dictionary of keywordarguments
            return f(*args, **kwargs)
        else:
            flash("Primero ingresa")
            return redirect(url_for("index"))
    return wrap


@app.route("/login/")
def login():
    try:
        return render_template("login.html")
    except Exception as e:
        return "error in the method login"+str(e)


@app.route("/data/", methods = ['GET','POST'])
@login_required
def data():
    try:
        return render_template("data.html")
    except Exception as e:
        return "error in the method data "+str(e)

@app.route("/introduce/", methods = ['GET','POST'])
def introduce():
    try:
        data= request.form
        users ={'felipe':'santos', 'sindel':'hernandez', 'admin':'password' }
        userna = data["username"].lower()
        passwo = data["password"].lower()
        if(userna in users):
            if(users[userna] in passwo ):
                session['username'] = userna
                session['password'] = passwo
	        return render_template("Introduce.html")
        flash("El usuario es incorrecto")
        return redirect(url_for("index"))
    except Exception as e:
        return "error in the method introduce "+str(e)


@app.route("/processData/", methods = ['GET','POST'])
@login_required
def processData():
    try:
        data= request.form
        return render_template("processData.html", data=data)
    except Exception as e:
        return "error in the method Process Data "+str(e)

@app.route("/exercices/", methods = ['GET','POST'])
@login_required
def exercices():
    try:
        return render_template("exercices.html", exercicesContent=exercicesContent)
    except Exception as e:
        return "error in the method exercices "+str(e)





@app.route("/warm_up/", methods = ['GET','POST'])
@login_required
def warm_up():
    try:
        return render_template("warm_up.html", exercicesWarmingUp=exercicesWarmingUp)
    except Exception as e:
        return "error in the method exercices "+str(e)


@app.route("/levels/", methods = ['GET','POST'])
#@login_required
def levels():
    try:
        return render_template("levels.html", levelsContent=levelsContent)
    except Exception as e:
        return "error in the method levels "+str(e)

@app.route("/send-mail/", methods = ['GET','POST'])
def send_mail():
    try:
	dataContact = request.form
	nameContact=dataContact["name"]
	emailContact=dataContact["email"]
	phoneContact= dataContact["phone"]
	messageContact=dataContact["message"]
	msg = Message(" Personal Training Message !"+str(nameContact), sender= "deliverymessage0gmail.com", recipients=["dniel096@gmail.com","ffelipecx@gmail.com"])
	msg.body = "Hello I am " +str(nameContact)+ " \n"+ "Message: "+str(messageContact) +" \nMy phone is: "+str(phoneContact)+ "\nMy email is: "+str(emailContact)
	mail.send(msg)
	flash("Your mail was sent")
	return redirect(url_for("index"))

    except  Exception as e:
	return str(e)


if(__name__=="__main__"):

    app.run(debug=True)
