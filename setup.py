#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx', 'rst.linker'] if needs_sphinx else []
needs_wheel = {'release', 'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

name = 'pmxbot.rss'
description = 'RSS feed support for pmxbot'

setup_params = dict(
	name=name,
	use_scm_version=True,
	author="YouGov, Plc.",
	author_email="opensource@yougov.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/yougov/" + name,
	packages=['pmxbot'],
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=[
		'feedparser',
		'pmxbot',
	],
	extras_require={
	},
	setup_requires=[
		'setuptools_scm>=1.9',
	] + pytest_runner + sphinx + wheel,
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
	],
	entry_points={
		'pmxbot_handlers': [
			'pmxbot feedparser = pmxbot.rss:RSSFeeds',
		],
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
