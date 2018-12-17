#!/usr/bin/python3

import os
import json

from adapters.dbconnector import AtomDB

class Map(object):
     """
     
     ST_Point(float x_lon, float y_lat)
     
     """
     def __init__(self):
          super(Map, self).__init__()

     def places(self, longitude, latitude, distance):
          """
          return [{}]
          """
          sql = ''' SELECT zip, address, email, work_phones, work_times, 
                    ST_AsGeoJSON(point), ST_Distance(point, 
                    ST_MakePoint({0}, {1})::geography) AS distance 
                    FROM atom_points 
                    WHERE ST_DWithin(point, ST_MakePoint({0}, {1})::geography, {2}) 
                    ORDER BY distance ASC'''.format(longitude, latitude, distance)

          content = []
          for item in AtomDB().execute(sql):
               data = {
                    'INDEKS': item[0],
                    'ADDRESS': item[1],
                    'EMAIL': item[2],
                    'TELEFON': item[3],
                    'REZHIM_RABOTY': item[4],
                    'DOLGOTA': json.loads(item[5])['coordinates'][0],
                    'SHIROTA': json.loads(item[5])['coordinates'][1]
               }
               content.append(data)
  
          return content

#-----------------------------------------------------------------------

if __name__ == '__main__':
     # print(Map().places(37.617635000000001, 55.755814000000001, 300_000))
     pass

#-----------------------------------------------------------------------