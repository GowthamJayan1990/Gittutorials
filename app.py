from flask import Flask

'''
Creates instance of Flask class, acting as  WSGI (Web Server Gateway Interface) application
'''
#WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this neww Flask course. This is in debug mode"

@app.route("/index")
def index():
    return "Welcome to the index page"


#Entry point of .py file
if __name__=="__main__":
    app.run(debug=True)