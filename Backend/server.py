from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route("/api/submit", methods=["POST"])
def submit_form():
    data = request.json
    print("Received Data:", data)
    return jsonify({"message": "Form submitted successfully!", "data": data})

if __name__ == "__main__":
    app.run(debug=True)
