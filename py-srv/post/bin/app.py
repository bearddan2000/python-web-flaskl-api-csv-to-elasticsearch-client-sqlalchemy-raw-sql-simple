from flask import Flask, request

from node import Node

app = Flask(__name__)

es_node = Node('elasticsearch')

@app.route('/')
def hello():
	return {"hello": "world"}

@app.route('/dog')
def get_all():
    return es_node.get_all()

@app.route('/dog/<dog_id>', methods=['GET', 'DELETE'])
def crud(dog_id):
    if request.method == 'GET':
        return es_node.filter_by(dog_id)
    
    return es_node.delete_by(dog_id)

@app.route('/dog/<dog_breed>/<dog_color>', methods=['PUT'])
def insert_entry(dog_breed, dog_color):
    return es_node.insert_entry(dog_breed, dog_color)

@app.route('/dog/<dog_id>/<dog_breed>/<dog_color>', methods=['POST'])
def update_entry(dog_id, dog_breed, dog_color):
    return es_node.update_entry(dog_id, dog_breed, dog_color)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
