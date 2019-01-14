#!/usr/bin/python3

import psycopg2
import psycopg2.extras

class AtomDB(object):
    def __init__(self):
        super(AtomDB, self).__init__()

        self._db_config = {
            'host': 'ec2-54-235-156-60.compute-1.amazonaws.com',
            'dbname': 'ded684tvpdf9gi',
            'user': 'wcskpxfmdwhqtp',
            'password': 'c5ae351b7e07a34fec9661fb9a03d173530e5727c013777a0acfa94fc4fb6cad'
        }
        
        self._db_connect = psycopg2.connect(**self._db_config)
        self._db_cursor = self._db_connect.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    def execute(self, sql: str):
        """ return [ { key_1: item_1 } ... ) ] """
        self._db_cursor.execute(sql)
        return self._db_cursor.fetchall()

    def __del__(self):
        self._db_connect.close()
        self._db_cursor.close()

#-----------------------------------------------------------------------

if __name__ == '__main__':
    
    pass
#-----------------------------------------------------------------------