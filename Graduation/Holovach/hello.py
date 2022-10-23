from flask import Flask
from flask import render_template
from analitics import Analitics


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table/')
@app.route('/table/<name>')
def table(name = "LOGS"):
    r= Analitics()
    to_html = r.query(name).to_html(index=False)
    text_t = open("templates/table.html", "w")
    text_t.write('<a href="/">Home</a><br>' + to_html)
    text_t.close()
    r.log("Table created")
    return render_template('/table.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    
    list_items = Analitics().query('LOGS')
    
    return render_template('hello.html', name=name , w = list_items)
