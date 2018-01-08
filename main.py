#!/usr/bin/python

import sys
import argparse
from HelpPage import helpPage

def main():
	parser = argparse.ArgumentParser(prog="MyBrew", description='Download program')
	# parser.add_argument('cmd', choices=['install', 'search'])
	parser.add_argument('install', metavar='install', type=str, nargs=1,
	                    help='install program')
	parser.add_argument('search', metavar='search', type=str, nargs=1,
	                    help='search program')
	parser.add_argument('name', metavar='name', type=str,
	                    help='The name of the program')
	parser.add_argument('--sum', dest='accumulate', action='store_const',
	                    const=sum, default=max,
	                    help='sum the integers (default: find the max)')

	args = parser.parse_args()
	print(args.accumulate(args.install))

	# if "-h" in sys.argv or "--help" in sys.argv:
	# 	helpPage.get_help()
	# elif len(sys.argv) == 1:
	# 	helpPage.get_help()
	# elif(len(sys.argv) == 2):
		# print("missing arg")


if __name__ == '__main__':
	main()