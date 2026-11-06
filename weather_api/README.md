# Weather API

A FastAPI project that returns the current temperature, humidity, and wind speed for a location. Choose between Open-Meteo and OpenWeather using the `provider` parameter.

## Run locally

From the `weather_api` directory, run these commands on Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Try a request

Keep the server running and open a second terminal. This example fetches the weather for Kermanshah using Open-Meteo:

```bash
curl 'http://127.0.0.1:8000/weather?lat=34.31&lon=47.07&provider=openmeteo'
```

The JSON response contains `temp` in °C, `humidity` in percent, and `wind_speed` in km/h. You can also try the endpoint in the [interactive API docs](http://127.0.0.1:8000/docs).

Open-Meteo requires no API key. To use OpenWeather, set the `OPENWEATHER_API_KEY` environment variable before starting the server and pass `provider=openweather` in the request.
