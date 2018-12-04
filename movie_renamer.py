# Simple script for renaming downloaded movie 
# torrent files to a predefined format
#
# Author: Emmanuel Macario
# Date: 04/12/18
# Version: v1.0

import sys
import argparse

def main():
    args = options()


def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', type=str,
        help="what is the name of the file?")
    parser.add_argument('-e', '--extra', type=bool, default=False,
        help="is the file remastered? (True/False)")

    args = parser.parse_args()
    #sys.stdout.write(str(rename(args)))
    return args




def rename(args):
    print(args.extra)


# Main program
if __name__ == "__main__":
    main()