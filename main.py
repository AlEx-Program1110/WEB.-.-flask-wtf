import json

from flask import Flask, url_for, render_template, request

app = Flask(__name__)
list_data_human = {'title': 'Анкета',
                   'surname': None,
                   'name': None,
                   'education': None,
                   'profession': None,
                   'sex': None,
                   'motivation': None,
                   'ready': None}

prof_list = {'profession9': 'гляциолог',
             'profession8': 'астрогеолог',
             'profession7': 'специалист по радиационной защите',
             'profession6': 'климатолог',
             'profession5': 'инженер по терраформированию',
             'profession4': 'врач',
             'profession3': 'экзобиолог',
             'profession2': 'строитель',
             'profession1': 'пилот',
             'profession0': 'инженер-исследователь'}


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
        prof = 'profession9 profession8 profession7 profession6 profession5 profession4 profession3 ' \
               'profession2 profession1 profession0'.split()
        for elem in prof:
            try:
                request.form[elem]
                prof = elem
                break
            except Exception:
                pass
        data = f'surname name education {prof} sex about accept'
        data = data.split()
        keys = list(list_data_human.keys())[1:]
        for i in range(len(data)):
            try:
                list_data_human[keys[i]] = request.form[data[i]]
                print(request.form[data[i]])
            except Exception:
                list_data_human[keys[i]] = None
        print(request.form)
        print(list_data_human)

        if list_data_human['ready'] == 'on':
            list_data_human['ready'] = True
        else:
            list_data_human['ready'] = False
        list_data_human['profession'] = prof_list[prof]
        return "Форма отправлена"


# answer
@app.route('/answer')
def answer():
    return render_template('answer.html', **list_data_human)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
