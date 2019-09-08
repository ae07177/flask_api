from flask import Flask,jsonify, request

app=Flask(__name__)
print(__name__)

projects = [ {'name':'openx', 'dir':'satya', 'id':1 } , {'name':'amobee', 'dir':'rk', 'id':2} ]

def valid_book_object(book_object):
	if ( "name" in book_object and "dir" in book_object and "id" in book_object ):
		return True
	else:
		return False
	

@app.route('/')
def hello_world():
	return "Hello World"

projs=[]
@app.route('/project', methods=['POST'])
def add_project():
	request_data = request.get_json()
	if(valid_book_object(request_data)):
		projs.extend(request_data)
		return "True"
	else:
		return "False"

@app.route('/project/<int:id>')
def get_project_by_id(id):
	ret_val = {}
	for project in projects:
		if project['id'] == id:
			ret_val = { 'name': project['name'], 'dir': project['dir'] }
	return jsonify(ret_val)

app.run(host='192.168.56.3',port='5000')
