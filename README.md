# pit-- Python as a stream filter

Version 0.3

pit is a stream filter for Python that makes it easier to use Python
in command line workflows.  It is designed to be a swiss army knife
for people who aren't as familiar with (or who don't want to deal with)
the entire array of Unix utilities. By default, lines of standard input
are piped into the underscore variable.

    >cat document.txt | pit 'math.log(len(_))'

## Installation:

sudo python setup.py install

----
##Instructions and example uses:

1. Quick command line calculator:

    >pit '.97**5 + random.random()'

2. Lines of standard input can be split by a delimiter (-d delimiter):

    >cat document.csv | pit -d , 'len(_[0])'

3. Standard input can be read as an entire page (-p):

    >cat document.txt | pit -p 'base64.encodestring(_)'

4. pit can filter incoming text literally. -f (filter) only prints lines that fulfill a boolean expression:

    >cat document.csv | pit -f 'len(_) > 10'
    >cat document.csv | pit -f 'random.random() > 0.9'

5. pit can be used to count unique occurences of lines in a document. -b allows for initialization code to be run before the loop, and -e executes, rather than evaluates, the code. An optional positional variable after the main code loop is executed after the loop is over:

    >cat redundant.txt | pit -b 'a=set()' 'a.add(_)' 'print len(a)'

## Known Issues:

- Newlines are stripped from standard input by calling strip(). This may cause collatoral damage on whitespace formatting.

## Changelog:
### What's new in version 0.3
* Autoimport support with [autoimp](github.com/autoimp). Dependency frozen at 1.0.4 for now.
* Runs on Python 3 
* Version flag

### What's new in version 0.2

* NOTE: expression evaluation is now default; -e now stands for _execute_ (necessary for variable assignment and multiline statements)
* -b flag can be used to execute code before loop
* optional positonal statement for code to be run after input is over

### What's new in version 0.1.1
* -d flag allows lines of standard input to be split up by a delimiter.
* -e flag evaluates command as an expression.
