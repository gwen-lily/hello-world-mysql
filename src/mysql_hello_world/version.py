"""scheme borrowed from:
https://github.com/mtchavez/python-package-boilerplate
apparently tests for coverage
"""


class Version:
    """An immutable Version of the package"""

    def __setattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    __delattr__ = __setattr__

    def __init__(self, num):
        super().__setattr__("_number", num)

    @property
    def number(self) -> str:
        """Return the version number"""
        return getattr(self, "_number")
