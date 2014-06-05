### Pit-- a Python command line piping tool

Pit is a tool for making it easier to run Python on the command line.
It is designed to be a swiss army knife for people who aren't as familiar with
(or who don't want to deal with) the entire array of Unix utilities.

----
##Example uses:

1. -e -> evaluates as expression 

    >pit -e ".97**12"

2. Lines of standard input are piped into the underscore variable, _

    >cat document.txt | pit "print len(_)"

3. Lines of standard input can be split up by a field separator:

    >cat document.csv | pit -fs , "print len(_[0])"

----
##What's next:

- A flag for taking whole file as one document (like -0777 in perl).