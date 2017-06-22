from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

Form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action"/" method = "post>
        <label for="form">
            <input type="text name="rot">0</input>
            <textarea name="text">
            <input type="submit" value="Submit"/>
        </label>
    </form>
    </body>
</html>
"""

@app.route("/", methods = ['POST'])
def index():
    return Form

@app.route("/", methods = ['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    text = int(text)
    return rotate_string(text, rot)

app.run()