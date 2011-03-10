# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
    name='arkpy',
    version='0.5',
    description="""Simple tools built around the Archival Resource Key
    and Noid specifications, allowing minting and validating of ARKs
    via code and the command-line.""",
    author="Michael J. Giarlo",
    author_email="leftwing@alumni.rutgers.edu",
    url="http://github.com/mjgiarlo/arkpy",
    py_modules=['arkpy', 'ez_setup'],
    test_suite='test',
    scripts=['bin/arkmint', 'bin/arkvalidate'])
