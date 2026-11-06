from fastapi import FastAPI, Query, HTTPException
import httpx
import os

app = FastAPI()

def get_openmeteo_weather(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
            "latitude" : lat,
            "longitude" : lon ,
            "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="Open-Meteo did not respond in time",
        ) from None
    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=502,
            detail="Open-Meteo returned an unsuccessful response",
        ) from None
    data = response.json()
    current = data["current"]

    return {
        "temp": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"]
    }

def get_openweather_weather(lat: float, lon:float):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OpenWeather API key is not configured"
        )
    url ="https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="OpenWeather did not respond in time"
        ) from None
    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=502,
            detail="OpenWeather returned an unsuccessful response",
        ) from None
    
    data = response.json()
    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]*3.6
    }


@app.get("/weather")
def get_weather(provider: str, lat: float = Query(..., ge = -90, le = 90), lon: float = Query(..., ge = -180 , le= 180)):

    if provider not in ("openweather", "openmeteo"):
        raise HTTPException(status_code=400, detail= "Use openweather or openmeteo")

    if provider == "openmeteo":
        return get_openmeteo_weather(lat, lon)
    return get_openweather_weather(lat , lon)
