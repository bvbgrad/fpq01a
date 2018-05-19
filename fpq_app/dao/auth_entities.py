"""
:summary Entity class using named tuple and attrs package
    pip install attrs
more information about the attrs package on its website at
    http://www.attrs.org/en/stable/
"""

import re

import attr
from attr import NOTHING


def required(message):
    def func(self, attr, val):
        if not val:
            raise ValueError(message)

    return func


def match(pattern, message):
    regex = re.compile(pattern)

    def func(self, attr, val):
        if val and not regex.match(val):
            raise ValueError(message)

    return func


@attr.s
class User(object):
    rowid = attr.ib(default=NOTHING)
    username = attr.ib(validator=required("Username required"))
    password = attr.ib()

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.rowid!r}, {self.username!r}')


@attr.s
class Score(object):
    rowid = attr.ib(default=NOTHING)
    when_taken = attr.ib()
    score = attr.ib()
    userIdFK = attr.ib()

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.rowid!r}, {self.when_taken!r}, {self.score!r}, '
                f'{self.userIdFK!r})')
