"""
REST API example endpoint.

Build your classes around this.
"""
import flask
import chat


@chat.mchat.route('/api/v1/', methods=['GET'])
def get_example():
    """
    Return example data with no meaning.
    """

    ouput = {}
    output['url'] = flask.request.path
    output['git_link'] = 'https://github.com/QMasterMoo/mchat'
    output['look_its_an_array'] = ['abc', 'def', '123', '456']
    output['its_just_json'] = true

    return flask.jsonify(**output)