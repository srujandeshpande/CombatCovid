import unittest

import src/wsgi as app

def test_test():
    assert app.build_test() == "Works!"
