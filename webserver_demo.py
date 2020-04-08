from flask import Flask, request, jsonify, Response
# Flask对象
app = Flask(__name__)

@app.route('/a', methods=['POST'])
def root():
    result = {
        'code': 0,
        'data': '',
        'msg': ''
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=6100,
        debug=True
    )