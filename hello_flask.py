from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login")
def index():
    return render_template("LOGINPAGE.html")

@app.route("/MAP.html")
def about():
    return render_template("MAP.html")

if __name__ == "__main__":
    app.run(debug=True)
