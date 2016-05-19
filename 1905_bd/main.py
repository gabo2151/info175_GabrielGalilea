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
	cur.execute("SELECT COUNT(gross_total) FROM sale WHERE [date] BETWEEN '2013-01-01' AND '2013-12-31'")

	rows = cur.fetchall()

	print "¿Cantidad total de ventas en el año 2013?"
	for row in rows:
		print row

	