#!/usr/bin/env python3

import os
import secrets
import logging

from datetime import date
from dotenv import load_dotenv
from logtail import LogtailHandler
from flask import Flask, render_template, redirect, url_for, request

load_dotenv()

handler = LogtailHandler(source_token=os.getenv('LOGTAIL_TOKEN'))

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.handlers = []
logger.setLevel(logging.INFO)
logger.addHandler(handler)


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

    logger.info(f'{name} has used the screener!')

    return render_template("screener.html", name=name, date=convert_datetime())

if __name__ == "__main__":
    app.run()
