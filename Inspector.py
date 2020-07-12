from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql
from config import *

con = pymysql.connect(HOST, USER, PASS, DATABASE)
inspector = Blueprint('inspector', __name__)


@inspector.route("/checkListDriver")
def CheckListDriver():
    if "username" not in session:
        return render_template('User/login.html', header_name="Login กรุณาเข้าใช้งาน")
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM `tbl_schedule_info` WHERE emp_driver_id != 0"
        cur.execute(sql)
        schedule_info_rows = cur.fetchall()
        return render_template("Inspector/checkListDriver.html", header_name = "Bus driver info", datas=schedule_info_rows)


@inspector.route("/checkListReception")
def CheckListReception():
    if "username" not in session:
        return render_template('User/login.html', header_name="Login กรุณาเข้าใช้งาน")
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM `tbl_schedule_info` WHERE emp_reception_id != 0"
        cur.execute(sql)
        schedule_info_rows = cur.fetchall()
        return render_template("Inspector/checkListReception.html", header_name = "Bus reception info", datas=schedule_info_rows)


@inspector.route("/submitCheckListDriver", methods=["POST"])
def SubmitCheckListDriver():
    if request.method == "POST":
        schedule_id = request.form["schedule_id"]
        crew_id = request.form['driver_id']
        emp_name = request.form['emp_name']
        emp_id = request.form['emp_id']
        emp_role = request.form['emp_role']
        driver_id = request.form['driver_id']
        driver_costume = request.form.get('check_costume')
        driver_license = request.form.get('check_license')
        driver_alcohol = request.form.get('check_alcohol')
        # if driver_costume == 'OK':
        #     print('yes')
        #     print(schedule_id)
        # else:
        #     print('no')
        if emp_role == 'พนักงานตรวจสอบ':
            with con:
                cur = con.cursor()
                sql = "INSERT INTO tbl_check_list (schedule_id, driver_id, driver_costume, driver_license, driver_alcohol,staff_id) VALUES (%s,%s,%s,%s,%s,%s)"
                cur.execute(sql, (schedule_id, crew_id, driver_costume, driver_license, driver_alcohol, emp_id))
                # cur.execute(sql)
                con.commit()
                return redirect(url_for('timetable.TimetableInfo'))
