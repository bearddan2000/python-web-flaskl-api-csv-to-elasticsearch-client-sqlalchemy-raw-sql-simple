from flask import Flask
from node import  Node

app = Flask(__name__)

if __name__ == "__main__":
    Node('elasticsearch')    
    app.run(host ='0.0.0.0', port = 5000, debug = True)
