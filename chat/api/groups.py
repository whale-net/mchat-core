"""
REST API endpoint for group listing.

Returns json list of 10 most recently created groups.
"""
import flask
import chat

from chat.api.util import make_404, 

@chat.mchat.route('/api/v1/g/', methods=['GET'])
def get_groups():
    """
    Return group listing per user.
    """
    if 'username' not in flask.session:
        return flask.jsonify(**{'message': 'Forbidden', 'status_code': 403})
    
    
