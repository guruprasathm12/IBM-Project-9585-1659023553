from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function


@app.route("/")
def index():
    return render_template("login.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       user_name = request.form.get("uname")
       # getting input with name = lname in HTML form
       email = request.form.get("email")
       number = request.form.get("number")
       return render_template("/pages.html",user_name=user_name, email=email, number=number)
 
if __name__=='__main__':
   app.debug = True
   app.run()