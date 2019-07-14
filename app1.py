from flask import Flask,jsonify

app=Flask(__name__)
print(__name__)

projects = [ {'name':'openx', 'dir':'satya' } , {'name':'amobee', 'dir':'rk'} ]

@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/project')
def project():
	return jsonify({'projects':projects})


app.run(host='192.168.56.3',port='5000')
