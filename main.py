import json

from flask import Flask, url_for, render_template, request

app = Flask(__name__)
list_data_human = {'title': None,
                   'surname': None,
                   'name': None,
                   'education': None,
                   'profession': None,
                   'sex': None,
                   'motivation': None,
                   'ready': None}


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    params = {
        'title': title,
    }
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = {
        'title': 'profession',
        'profession': prof
    }
    return render_template('prof.html', **params)


@app.route('/list_prof/<list_data>')
def list_prof(list_data):
    list_prof_data = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                      'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите', 'астрогеолог',
                      'гляциолог', 'инженер', 'жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                      'штурман', 'пилот', 'дронов']

    params = {
        'title': 'list_prof',
        'list': list_prof_data,
        'ol_ul': list_data
    }
    if list_data == 'ol':
        return render_template('list_prof.html', **params)
    elif list_data == 'ul':
        return render_template('list_prof.html', **params)
    else:
        return '<h1>ошибка (ol, ul)</h1>'


@app.route('/auto_answer', methods=['POST', 'GET'])
def auto_answer():
    if request.method == 'GET':
        return render_template('auto_answer.html')
    elif request.method == 'POST':
        data = 'file about sex profession9 profession8 profession7 profession6 profession5 profession4 profession3 ' \
               'profession2 profession1 profession0 education email name surname'
        data = data.split()
        data = data[::-1]

        for elem in data:
            try:
                list_data_human.append(request.form[elem])
            except Exception:
                pass
        return "Форма отправлена"


# answer
@app.route('/answer')
def answer():
    return render_template('answer.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
