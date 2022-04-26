#!/usr/bin/env python3

from datetime import date
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)



def convert_datetime():
    
    today = date.today()

    months = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }

    month = months[today.month]
    return f"{today.day} {month} {today.year}"




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/screener', methods=["GET", "POST"])
def screener():
    if request.method == "GET":
        return redirect(url_for("index"))
    
    name = request.form['name']
    date = convert_datetime()

    return render_template("screener.html", name=name, date=date)

if __name__ == "__main__":
    app.run(debug=True)
