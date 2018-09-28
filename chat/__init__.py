"""
MChat package initializer.

Alex Harding <alex.harding@whale-net.net>
"""
import flask

mchat = flask.Flask(__name__) # pylint: disable=invalid-name

# Load config
mchat.config.from_object('chat.config')

# give chat app access to api model and friends
import chat.api # pylint: disable=wrong-import-position
import chat.model # pylint: disable=wrong-import-position