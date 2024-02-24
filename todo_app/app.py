# app.py
from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    { "id": 1, "task": "Do laundry" },
    { "id": 2, "task": "Buy groceries" },
    { "id": 3, "task": "Clean the house" }
]

@app.route('/')
def index():
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
