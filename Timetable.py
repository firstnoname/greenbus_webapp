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


@timetable.route("/staffRegisterRoute", methods=["POST"])
def StaffRegisterRoute():
    if request.method == "POST":
        schedule_id = request.form["schedule_id"]
        emp_name = request.form['emp_name']
        emp_id = request.form['emp_id']
        emp_role = request.form['emp_role']
        if emp_role == 'พนักงานขับรถ':
            with con:
                cur = con.cursor()
                sql = "UPDATE tbl_schedule_info SET emp_driver_name = %s, emp_driver_id = %s WHERE schedule_id = %s"
                cur.execute(sql, (emp_name, emp_id, schedule_id))
                con.commit()
                return redirect(url_for('timetable.TimetableInfo'))
        else:
            with con:
                cur = con.cursor()
                sql = "UPDATE tbl_schedule_info SET emp_reception_name = %s, emp_reception_id = %s WHERE schedule_id = %s"
                cur.execute(sql, (emp_name, emp_id, schedule_id))
                con.commit()
                return redirect(url_for('timetable.TimetableInfo'))


@timetable.route("/staffUnregisteRoute", methods=["POST"])
def StaffUnregisterRoute():
    if request.method == "POST":
        schedule_id = request.form["schedule_id"]
        emp_name = request.form['emp_name']
        emp_id = request.form['emp_id']
        emp_role = request.form['emp_role']
        if emp_role == 'พนักงานขับรถ':
            with con:
                cur = con.cursor()
                sql = "UPDATE tbl_schedule_info SET emp_driver_name = '', emp_driver_id = '' WHERE schedule_id = %s"
                cur.execute(sql, (schedule_id))
                con.commit()
                return redirect(url_for('timetable.TimetableInfo'))
        else:
            with con:
                cur = con.cursor()
                sql = "UPDATE tbl_schedule_info SET emp_reception_name = '', emp_reception_id = '' WHERE schedule_id = %s"
                cur.execute(sql, (schedule_id))
                con.commit()
                return redirect(url_for('timetable.TimetableInfo'))
