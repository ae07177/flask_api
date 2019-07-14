from flask import Flask,jsonify

app=Flask(__name__)
print(__name__)

projects = [ {'name':'openx', 'dir':'satya', 'id':1 } , {'name':'amobee', 'dir':'rk', 'id':2} ]

@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/project')
def project():
	return jsonify({'projects':project})

@app.route('/project/<int:id>')
def get_project_by_id(id):
	ret_val = {}
	for project in projects:
		if project['id'] == id:
			ret_val = { 'name': project['name'], 'dir': project['dir'] }
	return jsonify(ret_val)

app.run(host='192.168.56.3',port='5000')
