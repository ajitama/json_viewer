# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for
from flask import request
import sys
import json
import glob


app = Flask(__name__)

@app.context_processor
def filelist():
    # ls data/
    return dict(ls_data=glob.glob("data/*"))


@app.route('/')
def top_route():
    return redirect(url_for('json_pp'))


@app.route('/viewer')
def json_pp():
    # URLの?以降を取得。 ( /viewer?file=hogehoge の hogehoge を変数filenameに代入)
    filename = request.args.get('file', default = None, type = str)

    file_json = filename
    try:
        fp_in = open (file_json,encoding='utf-8')
    except:
        # top、未指定の場合。
        return render_template('main.html',
                               title="json_sample",
                               json_rows=[{'col1':'data1-col1','col2':'data1-col2'},{'col1':'data2-col1','col2':'data2-col2'}]
                               )
    json_str = fp_in.read()
    fp_in.close()
    dict_aa = {}
    dict_aa = json.loads(json_str)
#
    rows = []
    for key in sorted (dict_aa.keys()):
        unit = dict_aa[key]
        unit['id'] = key
        rows.append(unit)

    #: rows total count
    total = len(rows)
    print("rows count : {}".format(total))


    return render_template('main.html', title=file_json, json_rows=rows)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

