from app import app
from flask import render_template

@app.route("/admin")
def admin():
    return "Hello i'm Admin"
