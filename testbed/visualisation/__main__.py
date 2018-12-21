import argparse
import os.path
from show_chain_without_datafile import visualize_without_datafile
from show_chain_with_datafile import visualize_with_datafile

parser = argparse.ArgumentParser()
parser.add_argument('--datafile', default='no')

args = parser.parse_args()

if args.datafile == 'no':
	visualize_without_datafile()
elif args.datafile != 'no':
	visualize_with_datafile(args.datafile)
