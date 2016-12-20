from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "I love sniping people on Black Ops 2"
    render = render_template('foo.html', greet=greeting)
    return render

if __name__ == "__main__":
    app.run()
