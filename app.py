from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    return f'<body style="background-color:{color};"><h1>Change Color</h1></body>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')