#!/usr/bin/env python

import re

kwES = {
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


def has_token(token, scrypt):
	p = re.compile('\\b' + token + '\\b')
	return p.search(scrypt)


def kws_to_EN(scrypt):
	for kw in kwES:
		if has_token(kw, scrypt):
			scrypt = scrypt.replace(kw, kwES[kw])

	return scrypt


