# env-1\Scripts\activate
# Set-ExecutionPolicy Unrestricted -Scope Process
# python app.py
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    print("At home route")
    return "<h1>Home page Changed</h1>"

if __name__=="__main__":
    
    print("==================Running==================")
    
    app.run(host="0.0.0.0")
    
    print("==================+++Off+++==================")