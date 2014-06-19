#!/usr/bin/env python

import sys
import errno
import argparse
import pdb
def run(cmd, args, text=''):
    global _
    if args.delimiter:
        _ = text.split(args.delimiter)
    else:
        _ = text

    if args.filter:
        out = eval(cmd, globals())
        if out:
            sys.stdout.write(text + '\n')

    elif args.execute:
        try:
            exec(cmd, globals())
        except IOError as e:
            if e.errno == errno.EPIPE:
                # receiving pipe closed
                return
    else:
        out = eval(cmd, globals())
        if out:
            sys.stdout.write(str(out) + '\n')

def init_args():
    parser = argparse.ArgumentParser(description='pit: a stream filter for Python')

    cant_both_execute_and_filter = parser.add_mutually_exclusive_group()
    cant_both_execute_and_filter.add_argument('-e', '--execute', action='store_true', help='Execute line as code rather than expressions.')
    cant_both_execute_and_filter.add_argument('-f', '--filter', action='store_true', help='Print lines from the input intact, if they fulfill the expression.')
    parser.add_argument('-d', '--delimiter', help='If included, the _ variable becomes standard input, split by the specified delimiter.')
    parser.add_argument('-p', '--page', action='store_true', help='Flag to read entire page into the _ variable.')
    parser.add_argument('-b', '--begin', help='Code to execute before the main loop. Regardless of the -e flag, this code is executed.')
    parser.add_argument('code', help='Code to evaluate (default) or execute (-e flag); each line of standard input is stored in the _ (underscore) variable.')
    parser.add_argument('end', nargs='?', help='Code to evaluate/execute after the main loop.')
    return parser.parse_args()

def write_to_stdout(out):
    try:
        sys.stdout.write(out + '\n')
    except IOError as e:
        if e.errno == errno.EPIPE:
            # receiving pipe closed
            return

def main():
    args = init_args()
    
    if args.begin:
        e_flag, f_flag = args.execute, args.filter
        args.execute = True
        run(args.begin, args)
        args.execute, args.filter  = e_flag, f_flag
    
    # nothing in standard in?
    if sys.stdin.isatty():
        run(args.code, args)
    
    # full page flag
    elif args.page:
        page = ''.join(sys.stdin.readlines())
        run(args.code, args, page)

    # standard looping
    else:
        for line in sys.stdin:
            if len(line) == 0:
                sys.stdout.flush()
                return
            run(args.code, args, line.strip())
    
    if args.end:
        run(args.end, args)

if __name__ == '__main__':
    main()
