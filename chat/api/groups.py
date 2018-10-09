"""
REST API endpoint for group listing.

Returns json list of 10 most recently created groups.
"""
import flask
import chat

from chat.model import get_group_listing

@chat.mchat.route('/api/v1/g/', methods=['GET'])
def get_groups():
    """
    Return group listing per user.
    """
    if 'username' not in flask.session:
        return flask.jsonify(**{'message': 'Forbidden', 'status_code': 403})
    context = {}
    context['url'] = flask.request.path

    groups = get_group_listing(flask.session['username'])
    context['groups'] = []
    for g in groups:
        context['groups'].append({
            'id': g[0],
            'name': g[1]
        })
    
    return flask.jsonify(**context)
