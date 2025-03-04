from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

prizes = ["Ring", "Chain", "Pendant", "Bali", "Tops", "Nath"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/lucky_draw', methods=['POST'])
def lucky_draw():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    prize = random.choice(prizes)
    return jsonify({"name": name, "phone": phone, "prize": prize})

if __name__ == '__main__':
    app.run(debug=True)
