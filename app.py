from flask import Flask, request, jsonify
import awsgi
import random

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "Unknown")
    temperature = f"{random.randint(15, 30)}°C"
    return jsonify({"city": city, "temperature": temperature})

def lambda_handler(event, context):
    return awsgi.response(app, event, context)
