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
		print "Ventas: "+str(row[0])
	print

	# Segunda pregunta
	print "¿Precio promedio de venta por producto?"
	cur.execute("SELECT avg(net_unit_price) AS promedio,  product.name FROM sale_product JOIN product WHERE product_id=product.id GROUP BY product.name ORDER BY name LIMIT 10")

	rows = cur.fetchall()
	for row in rows:
		print "Producto: " + str(row[1]) + "\nPrecio: $" + str(row[0])
	print

	# Tercera pregunta
	print "¿Total de ventas (gross_total) por cliente"
	cur.execute("SELECT COUNT(sale.gross_total), entity.names FROM sale JOIN entity WHERE sale.entity_id = entity.id GROUP BY entity.names LIMIT 10;")
	rows = cur.fetchall()
	for row in rows:
		print "Cliente/NumProductos: " + str(row[1]) + " - " + str(row[0])
	print

	# Cuarta pregunta
	print "¿Total de ventas por cliente en el año 2014?"
	cur.execute("SELECT COUNT(sale.gross_total), entity.names FROM sale JOIN entity WHERE sale.entity_id = entity.id AND date BETWEEN '2014-01-01' AND '2015-01-01' GROUP BY entity.names LIMIT 10;")
	rows = cur.fetchall()
	for row in rows:
		print "Cliente/NumProductos: " + str(row[1]) + " - " + str(row[0])
	print

	# Quinta pregunta
	print "¿Cantidad y monto total de ventas por día en noviembre de 2013?"
	cur.execute("SELECT date, COUNT(gross_total), SUM(gross_total) FROM sale WHERE date BETWEEN '2013-11-01' AND '2013-11-30' GROUP BY date ORDER BY date;")
	rows = cur.fetchall()
	for row in rows:
		print "Fecha: " + str(row[0]) + "\nCantidad/Monto: " + str(row[1]) + " - $" + str(row[2])
	print

	# Sexta pregunta
	print " ¿Cantidad y montos totales agrupados por producto en orden descendente según cantidad?"
	cur.execute("SELECT product.name, SUM(sale_product.quantity), SUM(sale_product.gross_total) FROM sale_product JOIN product WHERE sale_product.product_id = product.id GROUP BY product.name ORDER BY SUM(sale_product.quantity) DESC LIMIT 10;")
	rows = cur.fetchall()
	for row in rows:
		print "Producto: " + row[0] + "\nCantidad/Monto: " + str(row[1]) + " - $" + str(row[2])