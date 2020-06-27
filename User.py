from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql
from config import *

con = pymysql.connect(HOST, USER, PASS, DATABASE)
user = Blueprint('user', __name__)


@user.route("/login")
def UserLogin():
    return render_template("User/login.html")


@user.route("/checkLogin", methods=["POST"])
def CheckLogin():
    username = request.form['username']
    password = request.form['password']
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM tbl_employee WHERE emp_username = %s AND emp_password = %s"
        cur.execute(sql,(username, password))
        rows = cur.fetchall()
        print("จำนวนแถวในการเจอข้อมูล login = " + str(len(rows)))
        if len(rows) > 0:
            session['username'] = username
            session['firstname'] = rows[0][1]
            session['lastname'] = rows[0][2]
            session['emp_role'] = rows[0][3]
            session.permanent = True
            print(session)
            return redirect(url_for('timetable.TimetableInfo'))
        else:
            return "ไม่พบ username"

@user.route("/register")
def Register():
    return render_template("User/register.html")
