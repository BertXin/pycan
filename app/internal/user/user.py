from flask import  request, jsonify, render_template, abort

from app.internal.common.web.web import app
from app.internal.user.repository.repository import query_users_from_db
from app.utils.jtw import verify_token



@app.route('/user')
def user():
    return render_template('uesr.html')

@app.route('/query_users', methods=['GET'])
def query_users():
    token = request.headers.get('Authorization')
    if not token or not verify_token(token):
        abort(401)  # 未授权访问

    query_param = request.args.get('query', '')
    users = query_users_from_db(query_param)
    return jsonify(users)