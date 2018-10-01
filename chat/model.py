"""
MChat database api.
"""
import mysql.connector
import flask
import chat

from util.password import *

def create_user(username, display_name, avatar='', password):
    """
    Create a new user.
    """
    return ""

def verify_username_password(username, password):
    """
    Verify a user's password given their username.
    """
    cursor = get_db().cursor()
    cursor.execute(
        "SELECT password FROM Users WHERE username=?", (username,))
    )
    db_password_string = cursor.fetchone()['password']
    return verify_username_password(password, db_password_string)


def get_db():
    """
    Return database connection or open new one if not present.
    """
    if not hasattr(flask.g, 'mysql_db'):
        # please change password and username accordingly
        flask.g.mysql_db = mysql.connector.connect(
            user='mchatdev', 
            password='password',
            host='localhost',
            database=chat.mchat.config['DATABASE_NAME']
        )
    
    return flask.g.mysql_db

@chat.mchat.teardown_appcontext
def close_db(error):
    # pylint: disable=unused-argument
    """
    Close database on mchat termination.
    """
    if hasattr(flask.g, 'mysql_db'):
        try:
            flask.mysql_db.commit()
        except:
            # roll back in case of any errors when committing
            flask.mysql_db.roll_back()
        flask.mysql_db.close()