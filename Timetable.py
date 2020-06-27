from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql
from config import *

con = pymysql.connect(HOST, USER, PASS, DATABASE)
timetable = Blueprint('timetable', __name__)

@timetable.route("/timetableInfo")
def TimetableInfo():
    if "username" not in session:
        return render_template('User/login.html', header_name="Login กรุณาเข้าใช้งาน")
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM tbl_schedule_info"
        cur.execute(sql)
        schedule_info_rows = cur.fetchall()
        return render_template("Timetable/timetable_info.html", header_name = "Timetable Info", datas=schedule_info_rows, session=session)


@timetable.route("/busDriverInfo")
def BusDriverInfo():
    return render_template("Timetable/bus_driver_info.html", header_name = "Bus driver info")


@timetable.route("/busReceptionInfo")
def BusReceptionInfo():
    return render_template("Timetable/bus_reception_info.html", header_name = "Bus reception info")
