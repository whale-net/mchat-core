"""
MChat package initializer.

Alex Harding <alex.harding@whale-net.net>
"""
import flask

mchat = flask.Flask(__name__) # pylint: disable=invalid-name

# Load config from file
mchat.config.from_object('chat.config')
# Load config from environment variable
mchat.config.from_envvar('CHAT_SETTINGS', silent=True)

# give chat app access to api model and friends
import chat.api # pylint: disable=wrong-import-position
import chat.model # pylint: disable=wrong-import-position