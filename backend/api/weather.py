from backend.database.db import connect_db


def get_weather(city):
    connect_db()
    return f"Weather data for {city}"
