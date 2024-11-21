from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "The best way to predict the future is to invent it.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different."
]

@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
