#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

name = 'pmxbot.rss'
description = 'RSS feed support for pmxbot'

params = dict(
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
		'setuptools_scm>=1.15.0',
	],
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
	setuptools.setup(**params)
