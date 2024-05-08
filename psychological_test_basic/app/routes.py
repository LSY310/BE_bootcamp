from flask import Blueprint, jsonify, render_template, request, url_for
from .database import db
from .models import Participant, Answer
import pytz
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    # 참여자 정보 입력 페이지를 렌더링합니다.
    return render_template("index.html")


@main.route("/participants", methods=["POST"])
def add_participant():
    pass



@main.route("/question", methods=["get"])
def question():
    pass


@main.route("/submit", methods=["POST"])
def submit():
    pass



@main.route("/results")
def show_results():
    pass

