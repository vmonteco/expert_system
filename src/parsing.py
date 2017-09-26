#!/usr/bin/env python3

import re

################################################################################
#                                File parser                                   #
################################################################################

space_regex = re.compile(' |\t|\n')

def clean_line(l):
    """
    clean_line() removes possible comments and space characters (using
    space_regex from global scope).
    """
    
    return space_regex.sub( # replace occurences by first argument
        '',
        l.split('#')[0])


def parse(filename):
    """
    parse() parses the file content, interprets rules and initial states, and
    returns queries.
    """

    state = 0 # state permits to keep track of the parsing steps.
    
    with open(filename) as f:
        for line in f:
            line = clean_line(line) # removing comments and spaces
    return queries


if __name__ == '__main__':
    pass
