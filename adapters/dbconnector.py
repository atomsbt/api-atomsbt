#!/usr/bin/python3

import psycopg2
import psycopg2.extras

# -----------------------------------------------------------------------


class AtomDB(object):
    def __init__(self):
        super(AtomDB, self).__init__()

        self._db_config = {
            'host': 'ec2-54-247-118-238.eu-west-1.compute.amazonaws.com',
            'dbname': 'dsn9angbu9h92',
            'user': 'ohayrelqkdsthq',
            'password': 'a8cb96703e2f9ef40dadd0482bb503360e998fdf3207fb11b3e7f6011b3b3230'
        }

        self._db_connect = psycopg2.connect(**self._db_config)
        self._db_cursor = self._db_connect.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

    def execute(self, sql: str):
        """ :return: [ { key_1: item_1 }, ... ] """
        self._db_cursor.execute(sql)
        return self._db_cursor.fetchall()

    def execute_first(self, sql: str):
        """ :return: { key_1: item_1 } """
        self._db_cursor.execute(sql)
        array = self._db_cursor.fetchall()
        return array[0] if len(array) > 0 else None

    def __del__(self):
        self._db_connect.close()
        self._db_cursor.close()

# -----------------------------------------------------------------------


if __name__ == '__main__':
    pass
