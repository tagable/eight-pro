import argparse

def get_args():
	parser = argparse.ArgumentParser(prog="MyBrew", description='Download program')
	parser.add_argument('install', metavar='install', type=str, nargs='?',
	                    help='install program')
	parser.add_argument('package', metavar='package', type=str, nargs='+',
	                    help='The package of the program')

	args = parser.parse_args()
	return args.install, args.package
