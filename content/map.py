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
          sql = ''' SELECT zip, address, email, work_phones, work_times
                    , ST_AsGeoJSON(point) AS coord
                    , ST_Distance(point, ST_MakePoint({0}, {1})::geography) AS distance 
                    FROM atom_points 
                    WHERE ST_DWithin(point, ST_MakePoint({0}, {1})::geography, {2}) 
                    ORDER BY distance ASC'''.format(longitude, latitude, distance)

          content = []
          for item in AtomDB().execute(sql):
               data = {
                    'INDEKS': item.get('zip'),
                    'ADDRESS': item.get('address'),
                    'EMAIL': item.get('email'),
                    'TELEFON': item.get('work_phones'),
                    'REZHIM_RABOTY': item.get('work_times'),
                    'DOLGOTA': json.loads(item.get('coord')).get('coordinates')[0],
                    'SHIROTA': json.loads(item.get('coord')).get('coordinates')[1]
               }
               content.append(data)
  
          return content

#-----------------------------------------------------------------------

if __name__ == '__main__':
     # print(Map().places(37.617635000000001, 55.755814000000001, 300_000))
     pass

#-----------------------------------------------------------------------