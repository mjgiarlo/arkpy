# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
  	name = 'arkpy',
	version = '0.1',
	description = "a tool for working with Namaste directory description tags",
	author = "Daniel Coughlin",
	author_email = "dan.coughlin@gmail.com",
	url = "http://github.com/MaxFisher/arkpy",
	py_modules = ['arkpy', 'ez_setup'],
	test_suite = '',
	scripts = ['bin/arkmint', 'bin/arkvalidate']
)
