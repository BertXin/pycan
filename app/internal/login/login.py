from flask import request, jsonify, render_template

from app.internal.common.web.web import app
from app.internal.login.repository.repository import verify_login
from app.utils.jtw import generate_token


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_login(username, password):
            token = generate_token(username)
            return jsonify({"success": True, "token": token})
        else:
            return jsonify({"success": False}), 401
    return render_template('login.html')

token_blacklist = set()

@app.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token missing'}), 401

    # Check if the token is in the blacklist
    if token in token_blacklist:
        return jsonify({'message': 'Token already invalidated'}), 401

    # Add the token to the blacklist
    token_blacklist.add(token)
    return jsonify({'message': 'Logout successful'})

# Add a route to clear the blacklist (optional)
@app.route('/clear_blacklist', methods=['POST'])
def clear_blacklist():
    token_blacklist.clear()
    return jsonify({'message': 'Blacklist cleared'})