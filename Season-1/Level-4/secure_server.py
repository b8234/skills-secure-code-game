# secure_server.py

import os
from flask import Flask, request, jsonify
from secure_code import SecureStockDB

app = Flask(__name__)
log_mode = os.getenv("LOG_MODE", "secure")
db = SecureStockDB(log_mode=log_mode)

@app.route("/")
def index():
    return jsonify({
        "message": "SecureStockDB API",
        "endpoints": {
            "GET /stock-info": "/stock-info?symbol=MSFT",
            "GET /stock-price": "/stock-price?symbol=MSFT",
            "POST /update-price": {
                "payload": {"symbol": "MSFT", "price": 310.0}
            }
        }
    })

@app.route("/stock-info", methods=["GET"])
def stock_info():
    symbol = request.args.get("symbol")
    if not symbol:
        return jsonify({"error": "Missing 'symbol' parameter"}), 400

    result = db.get_stock_info(symbol)
    return jsonify({"response": result})

@app.route("/stock-price", methods=["GET"])
def stock_price():
    symbol = request.args.get("symbol")
    if not symbol:
        return jsonify({"error": "Missing 'symbol' parameter"}), 400

    result = db.get_stock_price(symbol)
    return jsonify({"response": result})

@app.route("/update-price", methods=["POST"])
def update_price():
    data = request.get_json(force=True)
    symbol = data.get("symbol")
    price = data.get("price")

    if not symbol or price is None:
        return jsonify({"error": "Both 'symbol' and 'price' are required"}), 400

    try:
        if not isinstance(price, float):
            raise ValueError("Price must be a float.")
        result = db.update_stock_price(symbol, price)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
