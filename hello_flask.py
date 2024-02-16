from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("LOGINPAGE.html")

@app.route("/dashboard", methods=['GET','POST'])
def status_page():
    return render_template('DASHBOARD.html')

@app.route("/device")
def device():
    return render_template("DEVICEMODEL.html")

@app.route("/individual")
def authentication_page():
    return render_template("INDIVIDUALPAGE.html")

if __name__ == "__main__":
    app.run(debug=True)