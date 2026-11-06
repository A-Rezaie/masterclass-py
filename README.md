# Python Project Portfolio

A collection of hands-on Python projects, including REST APIs, Flask web apps, and desktop tools.

## Featured projects

| Project | What it does |
| --- | --- |
| [Weather API](./weather_api/) | Returns temperature, humidity, and wind speed from Open-Meteo or OpenWeather. |
| [Products API](./products_api/) | Creates, lists, updates, and deletes products. Supports filtering by price. Products are stored in memory. |
| [Flask Portfolio](./flask-portfolio/) | A portfolio website built with Flask. |
| [Countdown Timer](./pyside_countdown_timer/) | A desktop countdown timer built with PySide. |

## Try the Weather API

From the repository root, run these commands on Linux or macOS:

```bash
cd weather_api
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open the [interactive API docs](http://127.0.0.1:8000/docs) while the server is running, or try this request in a second terminal:

```bash
curl 'http://127.0.0.1:8000/weather?lat=34.31&lon=47.07&provider=openmeteo'
```

This example fetches weather for Kermanshah and returns `temp`, `humidity`, and `wind_speed` as JSON. Open-Meteo works without an API key. To use OpenWeather, set the `OPENWEATHER_API_KEY` environment variable before starting the server.
