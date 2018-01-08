import argparse

def get_help():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('install', metavar='install', type=str, nargs='1',
	                    help='install program')
	parser.add_argument('Name', metavar='Name', type=int,
	                    help='The name of the program')
	parser.add_argument('--sum', dest='accumulate', action='store_const',
	                    const=sum, default=max,
	                    help='sum the integers (default: find the max)')

	args = parser.parse_args()
	print(args.accumulate(args.integers))