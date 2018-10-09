"""
MChat database api.
"""
import mysql.connector
import flask
import chat

from chat.util.password import *

def create_user(username, display_name, avatar, password):
    """
    Create a new user.
    """
    return ""

def verify_username_password(username, password):
    """
    Verify a user's password given their username.
    """
    cursor = get_db().cursor()
    query = ('SELECT password FROM Users WHERE username=\'%s\'' % (username))
    cursor.execute(query)
    db_password_string = cursor.fetchone()[0]
    cursor.close()
    return verify_password_str(password, db_password_string)

def get_group_listing(username):
    """
    Retrieve group id memberships.

    TODO: Add pagination
    """
    cursor = get_db().cursor()
    uid = get_uid_from_username(username)
    query = ('SELECT gid FROM Groups_Users WHERE uid=')

def get_uid_from_username(username):
    """
    Get uid from username.
    """
    cursor = get_db().cursor()
    query = ('SELECT uid FROM Users WHERE username=%s')
    cursor.execute(query, username)
    uid = cursor.fetchone()[0]
    cursor.close()
    return uid



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
            flask.g.mysql_db.commit()
        except:
            # roll back in case of any errors when committing
            flask.g.mysql_db.roll_back()
        flask.g.mysql_db.close()