#!/usr/bin/python
from flask import Flask, request, redirect, render_template, url_for
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


def auth_update(f):
	@wraps(f)
	def auth_dec(*args, **kwargs):
		return redirect('/Authenticate')	
	return auth_dec

@app.route('/update/<serial>/<name>',methods=['GET','POST'])
def update_db(serial,name):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * from users where serial ='" + serial + "' and name ='" + name + "'")	
	data = cur.fetchone()
	if data is None:
		return 'Authorization FAILED'
	else:
        	if request.method == 'POST':
                	userDetails = request.form
                	serial = userDetails['serial']
                	name = userDetails['name']
                	email = userDetails['email']
                	cur = mysql.connection.cursor()
                	cur.execute("INSERT INTO users(serial,name, email) VALUES(%s,%s, %s)",(int(serial),name, email))
                	mysql.connection.commit()
                	cur.close()
#                return redirect('/users')
                	return "SUCCESSFULLY UPDATED"
        	return render_template('index.html')


@app.route('/update', methods=['GET', 'POST'])
@auth_update
def update():
        if request.method == 'POST':
                pass
        return render_template('index.html')

@app.route('/users')
def users():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * from users")
        if resultValue > 0:
                userDetails = cur.fetchall()
                return render_template('users.html', userDetails=userDetails)

@app.route('/Authenticate', methods=['GET','POST'])
def Authenticate():
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
			return redirect(url_for('update_db',serial=serial,name=name))
        return render_template('index1.html')


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port='5000')
