# Simple script for renaming downloaded movie 
# torrent directories to a predefined format
#
# Author: Emmanuel Macario
# Date: 04/12/18
# Version: v1.0

import os
import sys
import argparse
import re

# SET THE PATH TO YOUR DEFAULT MOVIES DIRECTORY HERE
DEFAULT_PATH = "D:\Media\Movies\\"


def options():
    """
    Parse and return command-line arguments.

    --- Help Message: ---

    usage: movie_renamer.py [-h] [-n NAME] [-r REMASTERED] [-e EXTENDED]
                        [-d DIRECTORS]

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --name NAME  what is the name of the directory?
      -r REMASTERED, --remastered REMASTERED
                            is the film remastered? (t/f)
      -e EXTENDED, --extended EXTENDED
                            is this film the extended version? (t/f)
      -d DIRECTORS, --directors DIRECTORS
                            is this version the director's cut?

    ---------------------
    """
    # Create a new parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-n', '--name', type=str,
        help="what is the name of the directory?")
    parser.add_argument('-r', '--remastered', type=str, default='f',
        help="is the film remastered? (t/f)")
    parser.add_argument('-e', '--extended', type=str, default='f',
        help="is this film the extended version? (t/f)")
    parser.add_argument('-d', '--directors', type=str, default='f',
        help="is this version the director's cut?")

    # Parse and return command-line arguments
    return parser.parse_args()


def extract_data(name):
    """
    Given a movie torrent directory name, extracts
    the movie's 'title', 'year', and 'res', and 
    returns the data as a dictionary.
    """
    pattern = re.compile(r"""(?P<title>.+)                # Movie title
                             (?P<year>(19\d\d)|(20\d\d))  # Year released
                             .*\.                         # Extra info (e.g Remastered)
                             (?P<res>(\d){3,4}p)          # Resolution
                             """, re.VERBOSE)

    match = pattern.match(name)
    title = match.group('title')
    year = match.group('year')
    res = match.group('res')

    return {"title" : clean_title(title),
            "year" : year,
            "res" : res}


def clean_title(title):
    """
    Prepares the extracted title to be 
    used to re-name the directory.
    """
    # Replace full stops with whitespace, and 
    # remove leading and trailing whitespaces.
    title = title.replace('.', ' ')
    title = title.strip()

    return title


def new_dir_name(args, data):
    """
    Using the extracted data and parsed CMI,
    create and return the new name of the
    directory.
    """
    # Firstly, extract the movie data
    title = data['title']
    year = data['year']
    res = data['res']

    # Create the new directory name
    dir_name_str = title + ' (' + year + ')'

    if args.remastered == 't':
        dir_name_str += ' (Remastered)'
    if args.extended == 't':
        dir_name_str += ' (Extended)'
    if args.directors == 't':
        dir_name_str += ' (Director\'s Cut)'

    dir_name_str += ' [' + res + ']'

    return dir_name_str


def rename_dir(old_name, new_name):
    """
    Renames the chosen directory in the default specified path.
    """
    old_name = DEFAULT_PATH + old_name
    new_name = DEFAULT_PATH + new_name

    try:
        os.rename(old_name, new_name)
        print(new_name)
    except FileNotFoundError:
        print("Error, invalid file name.")



# MAIN PROGRAM
def main():
    args = options()
    data = extract_data(str(args.name))
    new_name = new_dir_name(args, data)
    rename_dir(str(args.name), new_name)


if __name__ == "__main__":
    main()