### Pit-- a Python command line piping tool

Pit is a wrapper that makes it easier to use Python in command line workflows.
It is designed to be a swiss army knife for people who aren't as familiar with
(or who don't want to deal with) the entire array of Unix utilities.

## Installation:

sudo python setup.py install

----
##Example uses:


1. Lines of standard input are piped into the underscore variable _

    >cat document.txt | pit "print len(_)"

2. Lines of standard input can be split up by a field separator:

    >cat document.csv | pit -fs , "print len(_[0])"

3. Quick command line evaluations (the -e flag evaluates the code as an expression)

    >pit -e ".97**12"

----
##What's next:

- A flag for taking whole file as one document (like -0777 in perl).
