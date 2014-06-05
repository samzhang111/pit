Pit-- a Python command line piping tool
=======================================

What's new
==========

* Lines of standard input can be split up by a field separator.
* -e flag evaluates command as an expression.

Pit is a tool for making it easier to run Python on the command line.
It is designed to be a swiss army knife for people who aren't as familiar with
(or who don't want to deal with) the entire array of Unix utilities.

Example uses:

Quick calculator
pit "print .97**12"

Lines of standard input are piped into the underscore variable, _

Prints out words per line
cat document.txt | pit "print len(_)"
