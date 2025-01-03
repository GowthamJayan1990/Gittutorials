from flask import Flask, render_template, request

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

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        return f"Hello {request.form['name']}"
    return render_template('form.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        return f"Hello {request.form['name']}"
    return render_template('form.html')

#Entry point of .py file
if __name__=="__main__":
    app.run(debug=True)