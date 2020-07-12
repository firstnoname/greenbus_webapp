from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql
from config import *

con = pymysql.connect(HOST, USER, PASS, DATABASE)
dataAnalys = Blueprint('dataAnalys', __name__)


@dataAnalys.route("/dataAnalys")
def DataAnalys():
    legend = 'Monthly Data'
    labels = []
    for index in range(30):
        labels.append(index)
    values = [40000, 35000, 38000, 30000, 28900, 60000, 58000, 39000, 51000, 54000,40000, 35000, 38000, 30000, 28900, 60000, 58000, 39000, 51000, 54000,40000, 35000, 38000, 30000, 28900, 60000, 58000, 39000, 51000, 54000]
    cost_values_maintainance = [170, 180,160,182,197,218,250,100,156,185,170, 180,160,182,197,218,250,100,156,185,170, 180,160,182,197,218,250,100,156,185]
    cost_values_fuel = [1600,1700,1800,1600,1500,1800,2500,1900,2700,1500,1600,1700,1800,1600,1500,1800,2500,1900,2700,1500,1600,1700,1800,1600,1500,1800,2500,1900,2700,1500]
    cost_values_driver = [213,300,260,280,300,450,500,200,270,250,213,300,260,280,300,450,500,200,270,250,213,300,260,280,300,450,500,200,270,250]
    cost_values_reception = [150,300,80,100,160,170,130,135,127,300]
    workday_driver =[22,22,18,20,22,24,20,17,19,23,22,22,18,20,22,24,20,17,19,23,22,22,18,20,22,24,20,17,19,23]
    workday_reception = [10,15,16,17,14,22,15,13,16,19,10,15,16,17,14,22,15,13,16,19,10,15,16,17,14,22,15,13,16,19]
    return render_template("DataAnalys/dataAnalysMainMenu.html", header_name="Data Analys",
        values=values,
        labels=labels,
        legend=legend,
        cost_values_maintainance=cost_values_maintainance,
        cost_values_fuel=cost_values_fuel,
        cost_values_driver=cost_values_driver,
        cost_values_reception=cost_values_reception,
        workday_driver=workday_driver,
        workday_reception=workday_reception)
