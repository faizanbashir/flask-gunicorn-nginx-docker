import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

application = Flask(__name__)

client = MongoClient(
    'mongodb://' os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@mongodb:27017/' + os.environ['MONGODB_DATABASE'],
    27017)
db = client.mintmesh

@application.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('index.html', items=items)

@application.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
