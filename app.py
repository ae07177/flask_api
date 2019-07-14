from flask import Flask

app=Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/project')
def project():
	return "AMOBEE"

app.run(host='192.168.56.3',port='5000')
