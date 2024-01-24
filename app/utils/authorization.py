from flask import make_response, jsonify, Flask

app = Flask(__name__, static_folder="../../static", template_folder="../../templates")

@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
