from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("LOGINPAGE.html")

@app.route("/status", methods=['POST'])
def status_page():
    return render_template('STATUS.html')

@app.route("/device")
def device():
    return render_template("DEVICEMODEL.html")

@app.route("/authentication")
def authentication_page():
    return render_template("AUTHENTICATION.html")

if __name__ == "__main__":
    app.run(debug=True)