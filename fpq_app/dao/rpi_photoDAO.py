"""
:summary Repository (Model) for photos
"""

from fpq_app.dao.rpi_entities import Photo

import logging

LOGGER_NAME = "my_app"


class PhotoRepository(object):
    def __init__(self, conn):
        self.app_logger = logging.getLogger(LOGGER_NAME)
        self.app_logger.info(str(__class__.__name__))
        self.conn = conn

    @staticmethod
    def to_values(c):
        return c.rowid, c.filename, c.comment, c.personIdFK

    def get_photos(self):
        self.app_logger.info(str(__class__.__name__))
        sql = "SELECT * FROM photo"
        for row in self.conn.execute(sql):
            photo = Photo(*row[0:])
            yield photo

    def add_photo(self, photo):
        self.app_logger.info(str(__class__.__name__))
        sql = "INSERT INTO photo VALUES (?, ?, ?, ?)"
        with self.conn:
            cursor = self.conn.cursor()
            # todo change print to a debug logging statement
            print("add_photo values: ", self.to_values(photo))
            cursor.execute(sql, self.to_values(photo))
            photo.rowid = cursor.lastrowid
        return photo

    def update_photo(self, photo):
        self.app_logger.info(str(__class__.__name__))
        sql = """UPDATE photo
                 SET _id = ?, filename = ?, comment = ?, personIdFK = ?
                 WHERE rowid = ?"""
        with self.conn:
            self.conn.execute(sql, self.to_values(photo) + (photo.rowid,))
        return photo

    def delete_photo(self, photo):
        self.app_logger.info(str(__class__.__name__))
        sql = "DELETE FROM photo WHERE rowid = ?"
        with self.conn:
            self.conn.execute(sql, (photo.rowid,))
