import flask
from flask import request, render_template, jsonify

from task5.search import search_by_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    return jsonify(search_by_query(request.json['query']))


app.run()
