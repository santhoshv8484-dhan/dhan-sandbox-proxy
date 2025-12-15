from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Read correct environment variables
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
    except Exception as e:
        return jsonify({"error": "Invalid JSON", "details": str(e)}), 400

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "client-id": CLIENT_ID
    }

    try:
        response = requests.post(DHAN_ENDPOINT, json=payload, headers=headers)
    except Exception as e:
        return jsonify({"error": "Request to Dhan failed", "details": str(e)}), 500

    try:
        return jsonify(response.json()), response.status_code
    except:
        return response.text, response.status_code


@app.route("/", methods=["GET"])
def home():
    return "Dhan Sandbox Proxy Running", 200
