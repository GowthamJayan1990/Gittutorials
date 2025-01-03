from flask import Flask, render_template

'''
Creates instance of Flask class, acting as  WSGI (Web Server Gateway Interface) application
'''
#WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')


#Entry point of .py file
if __name__=="__main__":
    app.run(debug=True)