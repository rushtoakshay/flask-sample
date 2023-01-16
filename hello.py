from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "<h1><!doctype html>
<head>
    <title>Hello Azure - Python Quickstart</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap/css/bootstrap.min.css') }}">
</head>
<html>
   <body>
     <main>
        <div class="px-4 py-3 my-2 text-center">
            <img class="d-block mx-auto mb-4" src="{{ url_for('static', filename='images/azure-icon.svg') }}" alt="Azure Logo" width="192" height="192"/>
            <!-- <img  src="/docs/5.1/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"> -->
            <h1 class="display-6 fw-bold">Hello {{name}}</h1>
            <p class="fs-5">
                It is nice to meet you!
            </p>
            <a href="{{ url_for('index') }}" class="btn btn-primary btn-lg px-4 gap-3">Back home</a>
          </div>
     </main>      
   </body>
</html></h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
