#Building url dynamically
#Variable rule
#Jinja 2 template engine

'''
    {{ }} expresiions to print output in html
    {% %} conditions, for loops
    {# #} comments
'''
from flask import Flask, render_template, request, redirect, url_for

'''
Creates instance of Flask class, acting as  WSGI (Web Server Gateway Interface) application
'''
#WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

'''
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        return f"Hello {request.form['name']}"
    return render_template('form.html')
'''

@app.route("/successres/<int:score>")
def successres(score):
    if score > 55:
        res="Passed"
    else:
        res="Failed"

    exp={"score":score,"res":res}
    
    return render_template('result1.html', results=exp)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', results=score)

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        cs = float(request.form['CS'])
        
        total_score = (maths+science+cs)/3
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('successres', score=total_score))



#Entry point of .py file
if __name__=="__main__":
    app.run(debug=True)