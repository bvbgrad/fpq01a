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
class Person(object):
    rowid = attr.ib(default=NOTHING)
    surname = attr.ib()
    # surname = attr.ib(validator=required("Surname required"))
    given_names = attr.ib()
    # given_names = attr.ib(validator=required("Given name(s) required"))
    sex = attr.ib()
    year_born = attr.ib()

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.rowid!r}, {self.surname!r}, {self.given_names!r}, '
                f'{self.sex!r}, {self.year_born!r})')


@attr.s
class Photo(object):
    rowid = attr.ib(default=NOTHING)
    filename = attr.ib()
    comment = attr.ib()
    personIdFK = attr.ib()

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.rowid!r}, {self.filename!r}, {self.comment!r}, '
                f'{self.personIdFK!r})')


@attr.s
class GedcomPerson(object):
    INDI_ID = attr.ib()
    surname = attr.ib()
    given_names = attr.ib()
    suffix = attr.ib()
    sex = attr.ib()
    birth_date = attr.ib()
    birth_place = attr.ib()
    death_date = attr.ib()
    death_place = attr.ib()
    spouse = attr.ib()
    mar_date = attr.ib()
    spouse2 = attr.ib()
    mar_date2 = attr.ib()
    spouse3 = attr.ib()
    mar_date3 = attr.ib()


@attr.s
class LivingPerson(object):
    day = attr.ib()
    month = attr.ib()
    year = attr.ib()
    first_name = attr.ib()
    middle_name = attr.ib()
    maiden_name = attr.ib()
    last_name = attr.ib()
    suffix = attr.ib()
    verify = attr.ib()
    nickname = attr.ib()
    sex = attr.ib()
    spouse_surname = attr.ib()
    spouse_given_names = attr.ib()
    marriage_date = attr.ib()
    # f1 = attr.ib()
    # f2 = attr.ib()
    # f3 = attr.ib()
    # f4 = attr.ib()
    # f5 = attr.ib()
