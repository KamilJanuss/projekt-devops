from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def strona_glowna():
    try:
        redis.incr('licznik')
        ile = redis.get('licznik').decode('utf-8')
        return f"Hej! To moj projekt na zaliczenie. Odwiedziny: {ile}"
    except Exception as e:
        return f"Blad polaczenia z baza: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)