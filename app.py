from flask import Flask, render_template

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return render_template('index.html')
