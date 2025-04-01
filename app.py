from flask import Flask, jsonify, request
import sys 


app = Flask(__name__)
port = sys.argv[1]

@app.route('/ping', methods=["GET"])
def ping():
    if (request.method == "GET"):
        return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=port)

