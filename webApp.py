from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/index.html')
def index():
    con = sqlite3.connect('childcare_data.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from location_data where GOV_REGION='London'")
    rows = cur.fetchmany(100)
    con.close()
    return render_template('index.html', rows=rows)