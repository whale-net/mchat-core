"""
MChat package initializer.

Alex Harding <alex.harding@whale-net.net>
"""
import flask

chat = flask.Flask(__name__) # pylint: disable=invalid-name

# Load config
chat.config.from_object('chat.config')

# give chat app access to api model and friends
import chat.api # pylint: disable=wrong-import-position
import chat.model # pylint: disable=wrong-import-position