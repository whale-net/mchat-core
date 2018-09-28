"""
MChat configuration.

Alex Harding <alex.harding@whale-net.net>
"""
import os

# Root of application, apparently useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Key for encrypting cookies, please regenerate before production, this is just so it works
SECRET_KEY = b'H\t\xea\xbc\x8e-T\x87B\x95\x1a#\x1a.\xd8\x99\x04\tF\xae\x93\x03U\xf0'

# path to image folder - not yet used
# ATTACHMENT_FOLDER = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
#     'var', 'uploads'
# )