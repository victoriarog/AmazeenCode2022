from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hi to all!</p>"

@app.route("/bye")
def tell_bye():
    return "<p>Bye to all!</p>"

@app.route("/data")
def get_data():
    clock_data = {
        "color": "red",
        "size" : "big",
        "type" : "analog",
        "arrows" : [1, 1, 1]
    }
    return clock_data

@app.route("/put-data")
def put_data():
    args = request.args
    name = args["name"]
    print(name)

    return {"result":"ok", "name": name }