import argparse
import os.path
from showChains import visualize_without_file

parser = argparse.ArgumentParser()
parser.add_argument('--datafile', default='no')

args = parser.parse_args()

if args.datafile == 'no':
	visualize_without_file()
elif args.datafile != 'no':
	visualize_without_file()