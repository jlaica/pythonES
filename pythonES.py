#!/usr/bin/env python

import argparse
from translator import kws_to_EN


class CustomError(Exception):
    def __init__(self, arg):
        self.msg = arg


def pytonES(file):
	if '.pyes' not in file:
		raise CustomError('Se necesita archivos .pyes')

	with open(file) as scryptSP:
		scryptSP = scryptSP.read()
		scryptEN = kws_to_EN(scryptSP)

	exec(scryptEN)


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Archivo .pyes", type=str)
	args = parser.parse_args()
	
	pytonES(args.file)


if __name__ == '__main__':
	Main()