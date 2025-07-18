from flask import Flask, request, jsonify
import random
import awsgi  # <--- для запуску у AWS Lambda

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "Unknown")
    temperature = f"{random.randint(10, 35)}°C"
    condition = random.choice(["Sunny", "Cloudy", "Rainy", "Windy"])
    return jsonify({
        "city": city,
        "temperature": temperature,
        "condition": condition
    })

# Вхідна точка для AWS Lambda
def lambda_handler(event, context):
    return awsgi.response(app, event, context)
