#!/usr/bin/env python

import sys
import errno
import argparse

def run(cmd, args, line='', _=''):
    if args.evaluate:
        out = eval(cmd)
        if args.filter and out:
            sys.stdout.write(line)
        elif out:
            sys.stdout.write(str(out) + '\n')
    else:
        try:
            exec(cmd)
        except IOError as e:
            if e.errno == errno.EPIPE:
                # receiving pipe closed
                quit()

def init_args():
    parser = argparse.ArgumentParser(description='Command line operations')
    parser.add_argument('-e', '--evaluate', action='store_true', help='Evaluate; evaluate line as expression rather than command.')
    parser.add_argument('-f', '--filter', action='store_true', help='Filter; print line if expression evaluates to true.')
    parser.add_argument('-fs', '--field-separator', default=',', help='Field separator; if included, _ becomes an array split by fs.')
    parser.add_argument('code', help='Command to run; line is stored in _ (underscore) variable')
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

    for line in sys.stdin:
        if len(line) == 0:
            sys.stdout.flush()
            quit()

        line = line.strip()
        if args.field_separator:
            _ = line.split(args.field_separator)
            cmd = args.code
        else:
            repr_line = repr(line)
            cmd = args.code.replace('_', format(repr_line))

        run(cmd, args, line, _)

if __name__ == '__main__':
    main()
