from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Load environment variables
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")

DHAN_ENDPOINT = "https://api-sandbox.dhan.co/orders"

@app.route("/place", methods=["POST"])
def place_order():
    if not ACCESS_TOKEN:
        return jsonify({"error": "DHAN_ACCESS_TOKEN not set"}), 500

    if not CLIENT_ID:
        return jsonify({"error": "DHAN_CLIENT_ID not set"}), 500

    try:
        payload = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "client-id": CLIENT_ID
    }

    response = requests.post(DHAN_ENDPOINT, json=payload, headers=headers)

    try:
        return jsonify(response.json()), response.status_code
    except:
        return response.text, response.status_code


@app.route("/", methods=["GET"])
def home():
    return "Dhan Sandbox Proxy Running", 200
