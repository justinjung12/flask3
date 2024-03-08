from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
import json
import random
alerts = []
currentalerts = ''

app = Flask(__name__)
def current_date_yyyymmdd():
    # 현재 날짜를 가져옴
    current_date = datetime.now()
    # 'yyyymmdd' 형태로 포맷팅하여 문자열로 변환
    formatted_date = current_date.strftime('%Y%m%d')
    return str(formatted_date)




@app.route('/')
def main():
    print(currentalerts)
    return render_template('schoolapp.html',alert= alerts, currentalert = currentalerts)
@app.route('/writealert',methods=['GET', 'POST'])
def writealert():
    global currentalerts
    if request.method == 'GET':
        return render_template('writealert.html')
    if request.method == 'POST':
        result = {}
        if request.form['pw'] == '123':
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts = result['text']
            return render_template('writealert.html')


