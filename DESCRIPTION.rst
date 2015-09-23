pit-- Python as a stream filter
=======================================

What's new in version 0.3
~~~~~~~~~~~~~
* Autoimport support with [autoimp](github.com/autoimp). Dependency frozen at 1.0.4 for now.
* Runs on Python 3 
* Version flag

What's new in version 0.2
~~~~~~~~~~~~~

* NOTE: expression evaluation is now default; -e now stands for _execute_
* -b flag can be used to execute code before loop
* optional positonal statement after loop

What's new in version 0.1.1
~~~~~~~~~~~~~
* Lines of standard input can be split up by a field separator.
* -e flag evaluates command as an expression.

Pit is a tool for making it easier to run Python on the command line.
It is designed to be a swiss army knife for people who aren't as familiar with
(or who don't want to deal with) the entire array of Unix utilities.

Example uses:
-------------

Quick calculator
~~~~~~~~~~~~~~~
::
    pit "math.log(.97**12)"


String processing
~~~~~~~~~~~~~~~
Lines of standard input are piped into the underscore variable, _
::
    cat document.txt | pit "_[::-1]" #Reverses all lines

Filter lines
~~~~~~~~~~~~~~
::
    cat document.txt | pit -f 'len(_) > 10' # Filter for long lines
    cat document.txt | pit -f 'random.random() > 0.5' # Sample lines from document with probability 0.5

Count unique occurences of lines in a document:
~~~~~~~~~~~~~~
The -e flag causes pit to execute the code, rather than evaluate it.
The -b flag (--begin) allows initialization code to be set up.
An optional positional argument after the main code section is run after the input ends.
::
    cat redundant.txt | pit -b 'a=set()' 'a.add(_)' 'print(len(a))'

Convert entire document to base64:
~~~~~~~~~~~~~~
The -p flag reads until EOF into the underscore variable.
::
    >cat document.txt | pit -p 'base64.encodestring(_)'

