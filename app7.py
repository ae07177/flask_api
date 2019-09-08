#!/usr/bin/python
from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
from functools import wraps
app = Flask(__name__)

## Configure DB
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/')
def index():
        return render_template('methods.html')


def Authenticate(function):
	@wraps(function)
#	@app.route('/Authenticate', methods=['GET','POST'])
#	def wrapper(*args, **kwargs):
	def wrapper(a):
        	if request.method == 'POST':
                	userDetails = request.form
                	serial = userDetails['serial']
                	name = userDetails['name']
                	cursor = mysql.connection.cursor()
                	cursor.execute("SELECT * from users where serial ='" + serial + "' and name ='" + name + "'")
                	data = cursor.fetchone()
                	if data is None:
                        	return index()
                	else:
				a = 1
                        	return function(a)
        	return render_template('index1.html')
	return wrapper

@app.route('/update1/a', methods=['GET', 'POST'])
def update1(a):
	if request.method == 'POST' and a == 1:
		userDetails1 = request.form
       		serial1 = userDetails1['serial']
       		email = userDetails1['email']
       		name1 = userDetails1['name']
       		cur = mysql.connection.cursor()
       		cur.execute("INSERT INTO users(serial,name, email) VALUES(%s,%s, %s)",(int(serial1),name1, email))
       		mysql.connection.commit()
       		cur.close()
#        	return render_template('users.html', userDetails=userDetails)
	return render_template('index.html')

@app.route('/update/<int:a>', methods=['GET', 'POST'])
@Authenticate
def update(a):
        if request.method == 'POST' and a == 1:
		return redirect(url_for('/update1/a')
#	return render_template('index.html')



@app.route('/users', methods=['GET','POST'])
def users():
        if request.method == 'POST':
		userDetails = request.form
                serial = userDetails['serial']
                name = userDetails['name']
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * from users where serial ='" + serial + "' and name ='" + name + "'")
                data = cursor.fetchone()
                if data is None:
			return "AUTHENTICATION FAILED"
		else:
        		cur = mysql.connection.cursor()
        		resultValue = cur.execute("SELECT * from users")
        		if resultValue > 0:
                		userDetails = cur.fetchall()
                		return render_template('users.html', userDetails=userDetails)
        return render_template('index1.html')

#@app.route('/Authenticate', methods=['GET','POST'])
#def Authenticate():
#        if request.method == 'POST':
#                userDetails = request.form
#                serial = userDetails['serial']
#                name = userDetails['name']
#                cursor = mysql.connection.cursor()
#                cursor.execute("SELECT * from users where serial ='" + serial + "' and name ='" + name + "'")
#                data = cursor.fetchone()
#                if data is None:
#                        return index()
#                else:
#                        return "Logged in successfully"
#        return render_template('index1.html')


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port='5000')
