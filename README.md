### Pit-- a Python command line piping tool

Pit is a stream filter for Python that makes it easier to use Python in command line workflows.
It is designed to be a swiss army knife for people who aren't as familiar with
(or who don't want to deal with) the entire array of Unix utilities.

    >cat document.txt | pit -e "len(_)"

By default, lines of standard input are piped into the underscore variable _, and the command argument that pit takes is executed as code. The -e flag evaluates the code as an expression instead (removing the need for a print statement).

## Installation:

sudo python setup.py install

----
##Example uses:

1. Lines of standard input can be split by a delimiter:

    >cat document.csv | pit -e -d , "len(_[0])"

2. Standard input can be read as an entire page:

    >cat document.txt | pit -p "print _[::-1]"

3. Pit can filter incoming text literally. -f (filter) only prints lines that fulfill a boolean expression:

    >cat document.csv | pit -f "len(_) > 10"
