#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
 
# TEST!!!!! 
#con = None
# 
#try:
#    con = lite.connect('test.db')
#    cur = con.cursor()    
#    cur.execute('SELECT SQLITE_VERSION()')
#    data = cur.fetchone()
#    print "SQLite version: %s" % data                
#except lite.Error, e:   
#    print "Error %s:" % e.args[0]
#    sys.exit(1)
#finally:    
#    if con:
#        con.close()
# END TEST!!!!!

con = lite.connect('pos_empresa.db')
with con:
	cur = con.cursor()

	# Primera pregunta
	print "¿Cantidad total de ventas en el año 2013?"
	cur.execute("SELECT COUNT(gross_total) FROM sale WHERE [date] BETWEEN '2013-01-01' AND '2013-12-31'")

	rows = cur.fetchall()
	for row in rows:
		print row

	# Segunda pregunta
	print "¿Precio promedio de venta por producto?"
	cur.execute("SELECT avg(net_unit_price) AS promedio,  product.name FROM sale_product JOIN product WHERE product_id=product.id GROUP BY product.name ORDER BY name LIMIT 10")

	rows = cur.fetchall()
	for row in rows:
		print row

	# Tercera pregunta
	