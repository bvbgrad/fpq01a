import os
import tempfile
import unittest

import fpq_app


class FpqAppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, fpq_app.config['DATABASE'] = tempfile.mkstemp()
        fpq_app.testing = True
        self.app = fpq_app.test_client()
        with fpq_app.app_context():
            fpq_app.init_db()


def tear_down(self):
    os.close(self.db_fd)
    os.unlink(fpq_app.config['DATABASE'])
    if __name__ == '__main__':
        unittest.main()
