from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Iris Model API is Running Successfully",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)