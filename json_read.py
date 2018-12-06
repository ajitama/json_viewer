# -*- coding: utf-8 -*-

from flask import Flask, render_template
import sys
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = "top page"
    return name


@app.route('/json')
def json_pp():
    file_json = "data/cities.json"
    fp_in = open (file_json,encoding='utf-8')
    json_str = fp_in.read()
    fp_in.close()
    dict_aa = json.loads(json_str)
#
    rows = []
    for key in sorted (dict_aa.keys()):
        unit = dict_aa[key]
        unit['id'] = key
        rows.append(unit)
#
    return render_template('main.html', title=file_json, cities=rows)

if __name__ == "__main__":
    app.run(debug=True)

