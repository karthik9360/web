from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login")
def index():
    return render_template("LOGINPAGE.html")

@app.route("/STATUS.html")
def about():
    return render_template("STATUS.html")
    
@app.route("/DEVICEMODEL.html")
def model():
    return render_template("DEVICEMODEL.html")
    
@app.route("/AUTHENTICATION.html")
def authen():
    return render_template("AUTHENTICATION.html")

if __name__ == "__main__":
    app.run(debug=True)