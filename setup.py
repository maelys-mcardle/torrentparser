"""The setup file for the BitTorrent parser.
"""

from setuptools import setup

setup(

    # General information.
    name='torrentparser',
    version='0.0.1',
    description='A parser for BitTorrent files.',
    url='https://github.com/maelys-mcardle/torrentparser',
    license='MIT',
    keywords='BitTorrent',

    # Author information.
    author='Maelys McArdle',
    author_email='spam@maelys.bio',

    # Classifiers (compatible version of Python, etc.)
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # The supported version of Python.
        'Programming Language :: Python :: 2.7',
    ],

    # Parser package.
    packages=['torrentparser'],

    # Where the unit tests are located.
    test_suite="tests",

    # Entry points.
    entry_points={
        'console_scripts': [
            'torrentparser=torrentparser:main',
        ],
    },
)