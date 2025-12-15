from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJwYXJ0bmVySWQiOiIiLCJkaGFuQ2xpZW50SWQiOiIyNTEyMTI2Njg3Iiwid2ViaG9va1VybCI6IiIsImlzcyI6ImRoYW4iLCJleHAiOjE3NjgxMTI2MDh9.FtOdHh6z4msBdebTrWZuZbCRKNzsPnFm2jN6FLK-1mZZS05lnXYlDs8YJddP1KXIwGycd3OO3lFsL4FbAfvogQ"
DHAN_ENDPOINT = "https://api-sandbox.dhan.co/orders"

@app.route("/place", methods=["POST"])
def place_order():
    try:
        payload = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.post(DHAN_ENDPOINT, json=payload, headers=headers)

    try:
        return jsonify(response.json()), response.status_code
    except:
        return response.text, response.status_code


@app.route("/", methods=["GET"])
def home():
    return "Dhan Sandbox Proxy Running", 200
