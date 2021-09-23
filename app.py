from flask import Flask, render_template, request,redirect, url_for
import requests
import json
from view import getdata,insert
from datetime import datetime,time

app = Flask(__name__)



@app.route('/data')
def date():
    stet = getdata()
    data = requests.get('https://gitlab.com/-/snippets/2094509/raw/master/sample_json_1.json')
    info = data.content
    data1 = json.loads(info)

    tall = 0
    for i in stet[::-1]:
        tall = tall + 1
        if tall >= 2:
            break

        try:
            startt = datetime.strptime(i[1],'%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            raise ValueError('Incorrect data format, should be %Y-%m-%dT%H:%M:%SZ')
        try:
            endt = datetime.strptime(i[2], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            raise ValueError('Incorrect data format, should be %Y-%m-%dT%H:%M:%SZ')
        if startt > endt:
            return render_template('404.html')

        start_t = startt.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_t = endt.strftime('%Y-%m-%dT%H:%M:%SZ')

        count = 0
        flag = 0
        swag = 0
        swim = 0
        ball = 0
        bale = 0
        for x in data1:
            datet = datetime.strptime(x['time'], '%Y-%m-%d %H:%M:%S')
            datetimee = datet.strftime('%Y-%m-%dT%H:%M:%SZ')
            d = datet.time()

            if d >= (datetime.strptime('06:00:00','%H:%M:%S')).time() and d < (datetime.strptime('14:00:00','%H:%M:%S')).time():
                shif = 'shiftA'
                if start_t <= datetimee <= end_t:
                    if x['production_A'] == True:
                        count = count + 1
                    if x['production_B'] == True:
                        flag = flag + 1


            if d >= (datetime.strptime('14:00:00','%H:%M:%S')).time() and d < (datetime.strptime('20:00:00','%H:%M:%S')).time():
                shif = 'shiftB'
                if start_t <= datetimee <= end_t:
                    if x['production_A'] == True:
                        swag = swag + 1
                    if x['production_B'] == True:
                        swim = swim + 1

            if d >= (datetime.strptime('20:00:00','%H:%M:%S')).time() or d < (datetime.strptime('6:00:00','%H:%M:%S')).time():

                shif = 'shiftC'
                if start_t <= datetimee<= end_t:
                    if x['production_A'] == True:
                        ball = ball + 1
                    if x['production_B'] == True:
                        bale = bale + 1


        sh = {
            'shiftA': {'production_A_count': count, 'production_B_count': flag},
            'shiftB': {'production_A_count': swag, 'production_B_count': swim},
            'shiftC': {'production_A_count': ball, 'production_B_count': bale},
        }
        json_object = json.dumps(sh,indent = 3)

        with open('abc.json','w') as file:
            file.write(json_object)


    return render_template('data.html',jsonfile=json.dumps(sh,indent = 3))

@app.route('/' ,methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        insert(start_time, end_time)
        return redirect(url_for('date'))


    return render_template('index.html')




if __name__ == '__main__':
    app.run()

