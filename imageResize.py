import sys, argparse, Image

parser = argparse.ArgumentParser(description='Resize some Images.')

parser.add_argument('-f', '--FILE', help='Enter a list of Filenames to be processed.')
parser.add_argument('-a', '--ALL', help='Resize ALL images in this directory.')