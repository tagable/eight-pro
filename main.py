#!/usr/bin/python

import sys
import argparse
from HelpPage import helpPage
from OSType.types import myOS

def main():
	cmd, packages_arr = helpPage.get_args()
	osName = myOS()
	print(osName.get_os_info(), cmd, packages_arr)
	if(cmd == "install"):
		print("Run install")
	elif(cmd == "search"):
		print("Run search")
	else:
		print("Other")


if __name__ == '__main__':
	main()