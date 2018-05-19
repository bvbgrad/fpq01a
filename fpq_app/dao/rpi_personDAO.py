"""
:summary Repository (Model) for persons
"""

from fpq_app.dao.rpi_entities import Person

import logging
LOGGER_NAME = "my_app"


class PersonsRepository(object):
    def __init__(self, conn):
        self.app_logger = logging.getLogger(LOGGER_NAME)
        self.app_logger.info(str(__class__.__name__))
        self.conn = conn

    def to_values(self, c):
        self.app_logger.info(str(__class__.__name__))
        return c.rowid, c.surname.title(), c.given_names, c.sex.upper(), int(c.year_born)
        # if c.year_born.isdigit():
        #     return c.rowid, c.surname.title(), c.given_names, c.sex.upper(), int(c.year_born)
        # else:  # todo ValueError if year_born is blank? or non-numeric?
        #     return c.rowid, c.surname.title(), c.given_names, c.sex.upper(), 0

    def get_persons(self):
        self.app_logger.info(str(__class__.__name__))
        sql = "SELECT * FROM person Order by surname, given_names"
        for row in self.conn.execute(sql):
            person = Person(*row[0:])
            yield person

    def get_person(self, person_id):
        self.app_logger.info(str(__class__.__name__))
        sql = "SELECT * FROM person WHERE _id = ?"
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(sql, person_id)
            person = cursor.lastrowid
        return person

    def add_person(self, person):
        self.app_logger.info(str(__class__.__name__))
        sql = "INSERT INTO person VALUES (?, ?, ?, ?, ?)"
        with self.conn:
            cursor = self.conn.cursor()
            # values_str = '|'.join(self.to_values(person))
            # self.app_logger.info("add_person values: ", values_str)
            print("add_person values: ", self.to_values(person))
            cursor.execute(sql, self.to_values(person))
            person.rowid = cursor.lastrowid
        return person

    def update_person(self, person):
        self.app_logger.info(str(__class__.__name__))
        sql = """UPDATE person
                 SET rowid = ?, surname = ?, given_names = ?, sex = ?, 
                 year_born = ? WHERE rowid = ?"""
        print(self.to_values(person))
        with self.conn:
            self.conn.execute(sql, self.to_values(person) + (person.rowid,))
        return person

    def delete_person(self, person):
        self.app_logger.info(str(__class__.__name__))
        sql = "DELETE FROM person WHERE rowid = ?"
        with self.conn:
            self.conn.execute(sql, (person.rowid,))
