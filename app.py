from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/html")

def hello_world():
    return "Hello World!"

@app.route("/name/<name>")
def hello_name(name):
    if name.lower()=='jan':
        return "Hello {}".format(name), 200
    else:
        return "Not Right Name", 404

@app.route("/integer/<int:value>")
def add_int(value):
    print value+1
    return "correct"

@app.route("/float/<float:value>")
def add_float(value):
    print value+1
    return "correct"

@app.route("/path/<path:value>")
def print_path(value):
    print value
    return value

if __name__ == "__main__":
    app.run()
