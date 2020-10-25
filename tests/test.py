from unittest.mock import patch


@patch('foo_pkg.foo.bar')
def test():
    assert True
