from flask import Flask, request,jsonify
from detect import inference

app = Flask(__name__)


# inference()


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/api/haptics/right', methods=['GET'])
def haptics_right():
    active = request.args.get('right', type=str).lower() == 'true'
    return jsonify({"right": active})


@app.route('/api/haptics/left', methods=['GET'])
def haptics_left():
    active = request.args.get('left', type=str).lower() == 'true'
    return jsonify({"left": active})

@app.route('/api/haptics', methods=['GET'])
def haptics():
    right_active = request.args.get('right', type=str).lower() == 'true'
    left_active = request.args.get('left', type=str).lower() == 'true'

    response = {
        "right_active": right_active,
        "left_active": left_active
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True) 