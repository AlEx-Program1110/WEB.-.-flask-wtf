import json

from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    params = {
        'title': title,
    }
    return render_template('index.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = {
        'title': 'profession',
        'profession': prof
    }
    return render_template('prof.html', **params)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
