from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello world";

@app.route('/about')
def about():
    return "This is about us page";



if __name__=="__main__":
    app.run()