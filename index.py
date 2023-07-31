from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/hello2")
def hello_world2():
    return "hello world 2"


@app.route("/h3/<name>")
def hello_world3(name):
    return "Hello %s!" % name


# app.add_url_rule("/", "hello2", "h2", hello_world2)


if __name__ == "__main__":
    app.run()
