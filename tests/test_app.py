import unittest

from src import wsgi as app

def test_test():
    assert app.build_test() == "Passed"
