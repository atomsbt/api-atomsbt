#!/usr/bin/python3

import psycopg2

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
        self._db_cursor = self._db_connect.cursor()

    def execute(self, sql):
        """ return [ ( item_1, item_2, ... ) ] """
        self._db_cursor.execute(sql)
        return self._db_cursor.fetchall()

    def __del__(self):
        self._db_connect.close()
        self._db_cursor.close()

#-----------------------------------------------------------------------

if __name__ == '__main__':
    
    # array1 = []
    # obj = {'pas': "password", 'login': "login"}
    # exc = 'select password, login from atom_users'
    # for row in AtomDB().execute(exc):
    #     array1.append({'password':row[0], 'login':row[1]})

    # print('-'*80)
    # print(array1)
    # print('-'*80)

    pass
#-----------------------------------------------------------------------