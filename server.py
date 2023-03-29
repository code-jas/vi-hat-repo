from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    data = {'message': 'Hello from the server!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)