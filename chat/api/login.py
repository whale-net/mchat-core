"""
REST API endpoint for logins.

User POSTs username and password.
"""
import flask
import json
import chat

from chat.model import verify_username_password


@chat.mchat.route('/api/v1/login/', methods=['POST'])
def post_login():
    """
    Log user in with POST request.
    """
    req = json.loads(flask.request.data.decode("utf-8"))
    username = req['username']
    password = req['password']
    context = {}
    
    # Log user in
    if verify_username_password(username, password):
        flask.session['username'] = username
        context['logged_in'] = True
        context['username'] = username
        return flask.jsonify(**context), 200
    
    context['message'] = 'Forbidden'
    context['status_code'] = 403
    return flask.jsonify(**context), 403