# This import will prevent the test patch from resolving the desired target in foo_pkg/foo.
# It will only find the function here imported as foo, not the module foo.
from .foo import foo
