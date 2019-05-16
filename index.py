""" --- index.py
--- Created by Patricia Nunes Dourado
--- May 15 of 2019;
 """
# coding: utf8

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests
import json

app = Flask(__name__)
Bootstrap(app)

weather_info = {
    'city' : 'undefined',
    'country' : 'undefined',
    'wind_speed' : 'undefined',
    'description': 'undefined',
    'temp': 'undefined',
    'temp_max' : 'undefined',
    'temp_min' : 'undefined'
    }          

@app.route('/',methods=['GET', 'POST'])
def index():
    purpose = 'Weather Finder'
    
    return render_template('index.html',purpose=purpose,weather_info=weather_info)
    
@app.route('/map',methods=['GET', 'POST'])
def map():
    purpose = 'Weather Info'
    error_msg = ''
    api_key = '01c331b462cd6dfb2abd515dffd14055'
        
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')
        
        if city and country:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}&units=metric'

            r = requests.get(url.format(city,country,api_key)).json()

            weather_info = {
                'city' : r['name'],
                'country' : r['sys']['country'],
                'wind_speed' : r['wind']['speed'],
                'description': r['weather'][0]['description'],
                'temp' : r['main']['temp'],
                'temp_max' : r['main']['temp_max'],
                'temp_min' : r['main']['temp_min']
                }
            
            print(weather_info)
        else:
            error_msg = 'Please enter the value.'
            return render_template('index.html',purpose=purpose,error_msg=error_msg)

    return render_template('map.html',purpose=purpose,weather_info=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
