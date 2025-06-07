from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/ping', methods=["GET"])
def ping():
    if (request.method == "GET"):
        return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

