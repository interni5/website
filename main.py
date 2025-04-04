from flask import Flask 
from flask import render_template
from flask import url_for


app = Flask(__name__)



@app.route('/')
def page_1():
    return render_template('index.html')

@app.route('/index1')
def page_2():
    return render_template('index1.html')

@app.route('/index2')
def page_3():
    return render_template('index2.html')

@app.route("/index3")
def page_4():
    return render_template("index3.html")

@app.route("/index4")
def page_5():
    return render_template("index4.html")




app.run(debug=True)