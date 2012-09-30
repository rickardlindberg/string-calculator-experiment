## The experiment

Your task is to implement a version of the string calculator.

The string calculator takes as input string containing an expression and
returns a number. The full specification for this version can be found in
`specs.py`.

You may implement it in any language.

The catch is that you can not test your code until you think you are done. So
you have to write the whole implementation, and when you think you are done,
you may test it against the spec.

You are allowed to fix errors once. But only once.

After completing this exercise, I would like you to answer the following
question: **What was different in your coding process when you knew you
couldn't test your code until you thought you were don?**

## How to test?

To be able to automatically test your program against the spec, it must read
the string expression from stdin and write the number to stdout. The number
should **not** be followed by newline. Before you start implementing your
solution, you may setup a template for your language of choice just to make
sure you got the interface right.

To test your code, first compile it if needed

    javac Template.java

then run the specs

    python specs.py java Template
    python specs.py [command to run your program]
