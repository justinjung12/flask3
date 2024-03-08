from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
from flask_cors import CORS
import json
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('schoolapp.html',currentalert = 'hi')
