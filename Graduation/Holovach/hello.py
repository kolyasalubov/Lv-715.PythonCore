# from crypt import methods
# from urllib import request
from flask import Flask, request
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

@app.route('/query/', methods=['POST', 'GET'])
# @app.route('/query/<name>')
def query(name = "LOGS"):
    r= Analitics()
    if request.method == 'POST':
        # table = request.form['table']
        return '-----'.join([ 'key : '+ x + '\t value : ' + y +'\n' for x,y in request.form.items()])
    else:
        return render_template('/query.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    
    list_items = Analitics().raw_query("SELECT * FROM LOGS")
    
    return render_template('hello.html', name=name , w = list_items)
