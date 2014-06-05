#!/usr/bin/env python

import sys
import errno
import argparse

def run(cmd, args, text=''):
    if args.delimiter:
        _ = text.split(args.delimiter)
    else:
        _ = text

    if args.filter:
        out = eval(cmd)
        if out:
            sys.stdout.write(text + '\n')

    elif args.expression:
        out = eval(cmd)
        if out:
            sys.stdout.write(str(out) + '\n')
    else:
        try:
            exec(cmd)
        except IOError as e:
            if e.errno == errno.EPIPE:
                # receiving pipe closed
                quit()

def init_args():
    parser = argparse.ArgumentParser(description='pit: a stream filter for Python')
    parser.add_argument('-e', '--expression', action='store_true', help='Evaluate line as expression rather than command.')
    parser.add_argument('-f', '--filter', action='store_true', help='Only print lines that fulfill the expression (assumes -e).')
    parser.add_argument('-d', '--delimiter', help='If included, _ becomes an array split by d.')
    parser.add_argument('-p', '--page', action='store_true', help='Store entire page rather than individual lines into _.')
    parser.add_argument('code', help='Command/expression to run; line is stored in _ (underscore) variable')
    return parser.parse_args()

def write_to_stdout(out):
    try:
        sys.stdout.write(out + '\n')
    except IOError as e:
        if e.errno == errno.EPIPE:
            # receiving pipe closed
            quit()

def main():
    args = init_args()

    # nothing in standard out?
    if sys.stdin.isatty():
        run(args.code, args)
        quit()
    
    if args.page:
        page = ''.join(sys.stdin.readlines())
        run(args.code, args, page)
        quit()

    for line in sys.stdin:
        if len(line) == 0:
            sys.stdout.flush()
            quit()

        line = line.strip()
        run(args.code, args, line)

if __name__ == '__main__':
    main()
