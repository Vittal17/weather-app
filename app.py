from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# OpenWeatherMap API key (replace with your own)
API_KEY = 'd976bfW02d3205a19e7e3c974554dda97'  

@app.route('/', methods=['GET'])
def index():
    city = request.args.get('city')  # Get city from query parameter
    weather_data = None
    error = None

    if city:
        # Call OpenWeatherMap API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
            weather_data = {
                'city': city,
                'temperature': round(temperature, 1)
            }
        else:
            error = f"Unable to fetch weather for {city}. Please check the city name."

    # Render the template with weather data or error
    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
