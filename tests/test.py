from unittest.mock import patch


# The patch errors with
# E AttributeError: <function foo at 0x10552b430> does not have the attribute 'bar'
@patch('foo_pkg.foo.bar')
def test():
    assert True
