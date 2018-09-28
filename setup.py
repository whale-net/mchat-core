# WIP
# i think i may have ab ugged python version

# """
# Setup for chat

# Alex Harding <alex.harding@whale-net.net>
# Connor Stabnick <connor.stabnick@whale-net.net>
# """
from setuptools import setup

setup (
    name="chat",
    version="0.0.1",
    packages=['chat'],
    include_package_data=True,
    install_requires=[
        'requests',
        'pylint',
        'flask',
    ],
)