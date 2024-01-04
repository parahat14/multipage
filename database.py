import mysql.connector
#pip install mysql-connector-python
import streamlit as st

conn = mysql.connector.connect(
host="localhost",
port="3306",
user="root",
passwd="",
db="das_cek")

c = conn.cursor()


def voucher_data():
	c.execute("select created_at,user,cpnyid,deptname,budget_cpnyid,actual_budget,topup from trx_voucher where status='C'")
	data = c.fetchall()
	return data

def view_all_departments():
	c.execute('SELECT Department FROM customers')
	data = c.fetchmany
	return data