from flask import Flask, session, render_template, redirect
from flask_session import Session
import random
import sys

app = Flask(__name__, static_folder='static')
app.secret_key = '123456'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def intro():
    session['number'] = 0
    data = get_survey_data()
    session['data'] = data
    return render_template('intro.html')


@app.route('/next_survey/<choose>')
def next_survey(choose):
    if 'number' not in session:
        return redirect('/')
    index = session['number']
    if index > 0:
        session['data'][index - 1]['choose'] = int(choose)
    session['number'] += 1
    if session['number'] > 10:
        return redirect('/end_survey')
    return redirect('/survey/' + str(session['number']))


@app.route('/survey/<number>')
def question_number(number):
    if 'number' not in session or not str(number) == str(session['number']):
        return redirect('/')
    current = session['data'][int(number) - 1]
    return render_template('survey.html', number=int(number), data=current)


@app.route('/end_survey')
def end_survey():
    result = {1: 0, 2: 0, 3: 0}
    for m in session['data']:
        method_index = int(m['video'][m['choose'] - 1][-5:-4])
        result[method_index] += 1
    with open('./static/result.csv', 'a') as file:
        file.writelines(['%d,%d,%d' % (result[1], result[2], result[3])])
        file.write('\n')
    if 'number' not in session:
        return redirect('/')
    return render_template('end.html')


def get_survey_data():
    data = []
    history = []
    while len(data) < 10:
        # 随机选题
        random_content = random.randint(1, 7)
        random_style = random.randint(1, 5)
        if (random_content, random_style) in history:
            continue
        # 随机排序1，2，3
        x = [1, 2, 3]
        random.shuffle(x)
        [m1, m2, m3] = x
        data.append({
            'content': '/static/content/c%d.mp4' % random_content,
            'style': '/static/style/%d.jpg' % random_style,
            'video': ['/static/video/c%d_s%d_m%d.mp4' % (random_content, random_style, m1),
                      '/static/video/c%d_s%d_m%d.mp4' % (random_content, random_style, m2),
                      '/static/video/c%d_s%d_m%d.mp4' % (random_content, random_style, m3)
                      ],
            'choose': 0
        })
        history.append((random_content, random_style))
    return data


if __name__ == '__main__':
    if len(sys.argv) > 1:
        app.run(sys.argv[1])
    else:
        app.run()
