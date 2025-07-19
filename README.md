# Weather App

Welcome to the Weather App, a simple Flask-based web application that fetches and displays the current temperature for any city using the OpenWeatherMap API!

## Description

This project is a beginner-friendly web app built to practice Flask, API integration, and GitHub workflows. Enter a city name, and the app retrieves the current temperature in Celsius, showcasing real-time weather data.

## Features

- Input a city name to get the current temperature.
- Displays temperature in Celsius, converted from Kelvin.
- Handles errors for invalid city names.
- Deployed using Flask with a basic HTML frontend.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

You'll also need an OpenWeatherMap API key (sign up at openweathermap.org/api).

## Installation

1. Clone the repository:
   `git clone https://github.com/Vittal17/weather-app.git`
   `cd weather-app`

3. Install the required packages:
   `pip install -r requirements.txt`

5. Set up your OpenWeatherMap API key (see "Usage" for secure setup).

6. Run the app:
   `python app.py`

8. Open your browser and go to `http://localhost:5000`.

## Usage

- Edit `app.py` and replace `"your_api_key_here"` with your OpenWeatherMap API key, or better yet, use an environment variable for security:
- Create a `.env` file with `API_KEY=your_api_key_here`.
- Install `python-dotenv` (`pip install python-dotenv`).
- Update `app.py` to read `os.environ.get('API_KEY')`.
- Add `.env` to `.gitignore` to keep it private.
- Enter a city name in the form and click "Get Weather" to see the temperature.

## Security Note

This project initially exposed the API key in the code. It’s recommended to revoke the exposed key via OpenWeatherMap and use environment variables to prevent future leaks. Check your account for unusual usage.

## Future Improvements

- Add more weather data (e.g., humidity, wind speed).
- Enhance the UI with CSS styling.
- Implement unit selection (Celsius/Fahrenheit).
- Add error handling for API rate limits.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests! Suggestions for new features or bug fixes are welcome.

## License

This project is open-source. Feel free to use and modify it under the MIT License.

## Acknowledgments

1. Built with guidance from xAI’s Grok.
- Powered by the OpenWeatherMap API.
