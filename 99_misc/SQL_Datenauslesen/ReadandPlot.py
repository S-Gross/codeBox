# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:17:57 2015

Die


@author: SGross
"""


import pymysql.cursors
import numpy as np



# Fix für beide Datenbanken
host = "d03.rz.rwth-aachen.de"
passwd = "3zzWa!bQ"
port=3303
user = "03_0008read"
db = "03_0008"


y_2015 = [
          "measurement201506",
          "measurement201507",
          "measurement201508",
          "measurement201509",
          "measurement201510",
          "measurement201511"]
          
y_2015_11 = ["measurement201511"]

total_length = []
elements_before_2015 = []


if __name__ == '__main__':
    # The connection to the database with the predefined parameter    
    connection = pymysql.connect(host=host, port=port, user=user, password=passwd, db=db, cursorclass=pymysql.cursors.DictCursor)
    
    with connection.cursor() as cursor:
        
        for ele in y_2015:
            cursor.execute("SELECT COUNT(*) FROM "+ ele +";")    
            #cursor.execute("SELECT * FROM measurement201511 WHERE timestamp < '2015-01-01 00:00:00'")    
            connection.commit()
            res = cursor.fetchall()
            total_length.append(res[0]["COUNT(*)"])
        
        
        for ele in y_2015:
            #cursor.execute("SELECT * FROM measurement201511 WHERE timestamp < '2015-01-01 00:00:00'")               
#            cursor.execute("SELECT * FROM " + ele + " WHERE timestamp =  '1980-01-01 01:00:00'")    
            cursor.execute("SELECT COUNT(*) FROM " + ele + " WHERE timestamp <  '2015-01-01 00:00:00'")    
            connection.commit()
            res = cursor.fetchall()
            elements_before_2015.append(res[0]["COUNT(*)"])
    
    # Wichtig aufräumen
    connection.close()

np_ele_b_2015 = []
np_total_length = []



for ele in total_length:
    np_ele_b_2015.append(np.array(elements_before_2015))
    np_total_length.append(np.array(total_length))

for idx, val in enumerate(total_length):
    res = np_ele_b_2015[idx]/np_total_length[idx]
    res = res * 100

