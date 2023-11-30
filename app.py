from flask import Flask,render_template
import requests
from dotenv import load_dotenv,dotenv_values
from sqlalchemy import create_engine, Integer,MetaData,Table, Column, String

metaData=MetaData
#definicion de tablas
cities = Table ('Cities',metaData,
               column('id', Integer(),primary_key=True,autoincrement=True),
               column('id',String(100), nullable=True, unique = True))


config = dotenv_values('.env')
app = Flask(__name__)
engine = create_engine("sqlite:///weather.db")

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric'
    r = requests.get(url).json()
    print(r)
    return r 

@app.route('/prueba')
def prueba():
    clima=get_weather_data('Ambato')
    temperatura = str (clima['main']['temp'])
    descripcion = str(clima['weather'][0]['description'])
    icono = str(clima['weather'][0]['icon'])

    r_json = {
              'cuidad' : 'Ambato',
              'temperatura': temperatura,
              'descripcion' : descripcion,
              'icono' : icono
         }
    return render_template('weather.html',clima = r_json)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clima')
def clima():
    return 'Clima'


if __name__ == '__main__' :
    app.run(debug=True)