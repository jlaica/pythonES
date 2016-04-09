# pythonES

La idea es correr archivos.pyes que son archivos de python escritos en español.

Como correr un archivo.pyes:

$ python pythonES.py miArchivo.pyes

* Una buena idea es darle permisos de ejecucion a pythonES.py, crear un symlink pythonES y poner el symlink en el PATH, para poder correr:

$ pythonES miArchivo.pyes

A continuacion un archivo .pyes 
que se podria correr con pythonES:

ejemplo.pyes

---------------------------------------------------------------
#!/usr/bin/env python

the_world_is_flat = 1
if the_world_is_flat:
	print "Be careful not to fall off!"

el_mundo_es_plano = 1
si el_mundo_es_plano:
	imprimir "Ten Cuidado de no caerte !!"

######################################################

a, b = 0, 1
while b < 10:
	print b
	a, b = b, a+b

a, b = 0, 1
mientras b < 10:
	imprimir b
	a, b = b, a+b

######################################################

x = 1
if x < 0:
	x = 0
	print 'Negative changed to zero'
elif x == 0:
	print 'Zero'
elif x == 1:
	print 'Single'
else:
	print 'More'

x = 1
si x < 0:
	x = 0
	imprimir 'Negativo cambiado a zero'
sino x == 0:
	imprimir 'Cero'
sino x == 1:
	imprimir 'Uno'
otro:
	imprimir 'Más'
---------------------------------------------------------------

Acepta los tokens en Ingles y en Español porque pythonES.py lo unico que hace es traducir todos los tokens en Español al Ingles con lo cual se consigue un script ejecutable por python.

Al momento pythonES solo puede traducir las keyWords de python, que estan definidas en el archivo translator.py




