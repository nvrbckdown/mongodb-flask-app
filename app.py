from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

db_host = host=os.environ['DB_HOST']
db_port = 27017

client = MongoClient(db_host, db_port)

db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))