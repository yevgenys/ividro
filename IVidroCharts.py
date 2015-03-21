from flask import Flask, render_template, jsonify

from dao.Dao import Dao

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summary')
@app.route('/summary/<int:limit>')
def get_last(limit=None):
    dao = Dao()
    if limit:
        return jsonify(log=dao.get(limit))
    return jsonify(log=dao.get())

