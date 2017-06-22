from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "post">
            <label for="rot">Rotate by:</label>
            <input type="text name="rot" value="0">
            <br>
            <textarea type="0" name="text">{0}</textarea>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    text = int(text)
    rotated_string = "<h1>" + rotate_string(text, rot) + "</h1>"
    return form.format(rotated_string)

app.run()