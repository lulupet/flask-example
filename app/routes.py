import json
import requests

from flask import jsonify, render_template, request

from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.form.to_dict()
    r = requests.get('https://api.agify.io?name=' + data['name'])
    return jsonify(age=json.loads(r.text)['age']), 200
