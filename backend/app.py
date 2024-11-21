from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "The best way to predict the future is to invent it.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different.",
    "預測未來的最好方法就是去創造它。",
    "代碼就像幽默。當你不得不解釋它時，它就不好了。",
    "經驗是每個人給他們錯誤的名字。",
    "為了不可替代，一個人必須總是與眾不同。",
    "Cara terbaik untuk meramalkan masa depan adalah dengan menciptanya.",
    "Kod adalah seperti humor. Apabila anda perlu menjelaskannya, ia tidak baik.",
    "Pengalaman adalah nama yang diberikan semua orang kepada kesilapan mereka.",
    "Untuk menjadi tidak boleh digantikan, seseorang mesti sentiasa berbeza."
]

@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
