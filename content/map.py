#!/usr/bin/python3

import os
import json
import psycopg2

class Map(object):
     """ST_Point(float x_lon, float y_lat)"""
     def __init__(self):
          super(Map, self).__init__()

          self.host='ec2-54-235-156-60.compute-1.amazonaws.com'
          self.dbname='ded684tvpdf9gi'
          self.user='wcskpxfmdwhqtp'
          self.password='c5ae351b7e07a34fec9661fb9a03d173530e5727c013777a0acfa94fc4fb6cad'

          _content = {
               "INDEKS": "215430",
               "ADDRESS": "Смоленская область п.Угра Новоселов 1",
               "TELEFON": [
                    "+7 (4813) 74-1869"
               ],
               "EMAIL": "client@smolensk.atomsbt.ru",
               "REZHIM_RABOTY": [
                    "пн - чт: с 09:00 по 18:00 Обед с 13:00 по 13:45",
                    "пт: с 09:00 по 16:45 Обед с 13:00 по 13:45"
               ],
               "SHIROTA": 54.777993,
               "DOLGOTA": 34.319726
          }

     def places(self, longitude=None, latitude=None, distance=None):
          if longitude == None or latitude == None or distance == None : return []

          bd_address = "host={0} dbname={1} user={2} password={3}".format(self.host, self.dbname, self.user, self.password)

          db = psycopg2.connect(bd_address)
          cursor = db.cursor()

          ex = 'SELECT zip, address, email, work_phones, work_times, ST_AsGeoJSON(point), ST_Distance(point, ST_MakePoint({0}, {1})::geography) AS distance FROM atom_map_points WHERE ST_DWithin(point, ST_MakePoint({0}, {1})::geography, {2}) ORDER BY distance ASC'.format(longitude, latitude, distance)
          cursor.execute(ex)

          content = []
          for zip, address, email, work_phones, work_times, point, dis in cursor:
               data={
                    'INDEKS':zip,
                    'ADDRESS':address,
                    'EMAIL':email,
                    'TELEFON':work_phones,
                    'REZHIM_RABOTY':work_times,
                    'DOLGOTA':json.loads(point)['coordinates'][0],
                    'SHIROTA':json.loads(point)['coordinates'][1]
               }
               content.append(data)

          cursor.close()
          return content

#-----------------------------------------------------------------------

if __name__ == '__main__':
     # print(Map().places(37.617635000000001, 55.755814000000001, 300_000))
     pass

#-----------------------------------------------------------------------