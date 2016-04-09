#!/usr/bin/python

import argparse
import re

kw = {
'y'          : 'and',
'como'       : 'as',
'afirmar'    : 'assert',
'terminar'   : 'break',
'clase'      : 'class',
'continuar'  : 'continue',
'func'       : 'def',
'eliminar'   : 'del',
'sino'       : 'elif',
'otro'       : 'else',
'excepto'    : 'except',
'exec'       : 'exec',
'finalmente' : 'finally',
'por'        : 'for',
'desde'      : 'from',
'global'     : 'global',
'si'         : 'if',
'importar'   : 'import',
'en'         : 'in',
'es'         : 'is',
'lambda'     : 'lambda',
'no'         : 'not',
'o'          : 'or',
'pasar'      : 'pass',
'imprimir'   : 'print',
'producir'   : 'raise',
'retornar'   : 'return',
'probar'     : 'try',
'mientras'   : 'while',
'con'        : 'with',
'dar'        : 'yield',
}

class CustomError(Exception):
    def __init__(self, arg):
        self.msg = arg

def isKeyWord(skw, scrypt):
	p = re.compile('\\b'+skw+'\\b')
	return p.search(scrypt)
	

def foo(file):
	if '.pyes' not in file:
		raise CustomError('Se necesita archivos .pyes')
		
	else:
		with open(file) as scrypt:
			scrypt = scrypt.read()
			for skw in kw:
				if isKeyWord(skw, scrypt):
					scrypt = scrypt.replace(skw, kw[skw])
	
	exec(scrypt)


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Archivo pyec", type=str)
	args = parser.parse_args()
	foo(args.file)

if __name__ == '__main__':
	Main()

































