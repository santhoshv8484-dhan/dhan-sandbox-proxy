from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Read from PythonAnywhere environment variables
ACCESS_TOKEN = os.getenv("eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJwYXJ0bmVySWQiOiIiLCJkaGFuQ2xpZW50SWQiOiIyNTEyMTI2Njg3Iiwid2ViaG9va1VybCI6IiIsImlzcyI6ImRoYW4iLCJleHAiOjE3NjgxMTI2MDh9.FtOdHh6z4msBdebTrWZuZbCRKNzsPnFm2jN6FLK-1mZZS05lnXYlDs8YJddP1KXIwGycd3OO3lFsL4FbAfvogQ")
CLIENT_ID = os.getenv("2512126687")

DHAN_ENDPOINT = "https://api-sandbox.dhan.co/orders"

@app.route("/place", methods=["POST"])
def place_order():
    if ACCESS_TOKEN is None:
        return jsonify({"error": "DHAN_ACCESS_TOKEN not set"}), 500

    if CLIENT_ID is None:
        return jsonify({"error": "DHAN_CLIENT_ID not set"}), 500

    try:
        payload = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Dhan requires client-id header
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
