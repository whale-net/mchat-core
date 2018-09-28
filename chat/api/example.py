"""
REST API example endpoint.

Build your classes around this.
"""
import flask
import chat


@chat.mchat.route('/api/v1/example/', methods=['GET'])
def get_example():
    """
    Return example data with no meaning.
    """

    context = {}
    context['url'] = flask.request.path
    context['git_link'] = 'https://github.com/QMasterMoo/mchat'
    context['look_its_an_array'] = ['abc', 'def', '123', '456']
    context['its_just_json'] = True

    return flask.jsonify(**context)