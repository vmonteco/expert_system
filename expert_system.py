#!/usr/bin/env python3

import argparse
import src.parsing

################################################################################
#                              Command parser                                  #
################################################################################

def make_parser():
    """
    make_parser() just generates the expert_system.py arguments parser.
    """

    parser = argparse.ArgumentParser(description='Inference engine.')
    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True
    solver_subparser = subparsers.add_parser('run')
    solver_subparser.add_argument(
        '-v', '--verbose', help='enable verbose mode.', action='store_true'
    )
    solver_subparser.add_argument(
        '-d', '--debug', help='enable debug mode.', action='store_true'
    )
    solver_subparser.add_argument(
        'filename', type=str,
        help='filename containing the instructions to process.'
    )
    return parser

def run(filename, verbose, debug):
    """
    Empty function so far.
    """
    queries = src.parsing.parse(filename)


################################################################################
#                                Entrypoint                                    #
################################################################################

if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    if args.subcommand == 'run':
        run(args.filename, verbose=args.verbose, debug=args.debug)
