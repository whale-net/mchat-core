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
    context['groups'] = []

    # Retreive query variables
    query_num_groups = flask.request.args.get('size') 
    query_page = flask.request.args.get('page')  
    num_groups = int(query_num_groups) if query_num_groups != None else 10
    page_number = int(query_page) if query_page != None else 0

    groups = get_group_listing(flask.session['username'], 
                               num_groups, page_number)
    for g in groups:
        context['groups'].append({
            'id': g[0],
            'name': g[1]
        })

    if (num_groups == 10):
        context['next'] = '{}?page={}'.format(context['url'], page_number + 1)
    else:
        context['next'] = '{}?page={}&size={}'.format(context['url'], 
                                                page_number + 1, num_groups)

    return flask.jsonify(**context)
