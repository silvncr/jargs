from jargs import __version__

from setuptools import setup

setup(
	name='jargs',
	version=__version__,
	description='simplifying args jargon',
	long_description=open('README.md', 'r').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/silvncr/jargs',
	author='silvncr',
	include_package_data=True,
	license='MIT',
	packages=['jargs'],
	package_data={},
	setup_requires=['pytest_runner'],
	python_requires='>=3.6',
	scripts=[],
	tests_require=['pytest'],
	entry_points={},
	zip_safe=True,
	classifiers=[
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
