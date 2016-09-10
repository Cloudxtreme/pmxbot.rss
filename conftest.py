import urllib.request

import pytest

@pytest.fixture(scope='session')
def internet():
	try:
		urllib.request.urlopen('https://www.google.com')
	except Exception:
		pytest.skip("Internet not available")


@pytest.fixture(params=['mongodb', 'sqlite'])
def db_uri(request):
	if request.param == 'mongodb':
		return request.getfuncargvalue('mongodb_uri')
	return 'sqlite:pmxbot.sqlite'
