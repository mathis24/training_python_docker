#!/usr/bin/env python3

# example of usage (order of arguments does not matter):
#   test_argparse.py --help 
#   test_argparse.py --version 
#   test_argparse.py -a 12
#   test_argparse.py --arg-example 12
#   test_argparse.py --arg-example 12 myfile
#   test_argparse.py --arg-example 12 -t myfile

import argparse

parser = argparse.ArgumentParser()


parser.add_argument('-o', action='store', 
                    dest='simple_value', # not mandatory, if not present, result put in results.o
                    help='Store a simple value')

parser.add_argument('-a', "--arg-example", action='store',
                    required=True,
                    type=int,
                    help='Store a simple value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

parser.add_argument("filename", action='store', 
                    nargs='?',  # means arg not mandatory
                    help='filename prefix (stdout if not provided)')

results = parser.parse_args()
print(results)
print('simple_value     =', results.simple_value)
print('simple_value2    =', results.arg_example)
print('boolean_switch   =', results.boolean_switch)
print('filename         =', results.filename)

