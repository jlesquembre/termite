.. include:: links.rst

=================================
Calling external python functions
=================================


Command line is great, but sometimes is useful to write python code to do
some tasks. `Termite`_ provides a command line utility, called tcli, to help
you with that.

First, write a python file with your utilities, call this file
`termite_cli.py`, and put this file in the same directory where your `termite.yaml`
resides.

A simple `termite_cli.py` file:

.. code-block:: py

    def hello(args):
        print ('Hello, your arguments are: ', args)


Now, from the command line, run this:

.. code-block:: bash

    tcli hello -x 5


`Termite`_ is going to call the function `hello` in the file `termite_cli.py`.
All the arguments after the function name, are saved in a python list and
passed to the function. In our case the value of `args` is `['-x', '5']`

Call the `hello` function from a `Termite`_ file with this task:

.. code-block:: yaml

    - shell:
        command: tcli hello the arguments


Lets write a more complicated `termite_cli.py` file:

.. code-block:: py

    import os
    from docopt import docopt
    from jinja2 import Environment, FileSystemLoader

    def render(args):
        usage = '''Usage: render (--input IN) (--output OUT) [<vars>...]'''

        arguments = docopt(usage, argv=args)
        variables = dict([var.split('=') for var in arguments['<vars>']])

        env = Environment(loader=FileSystemLoader(os.getcwd()))
        template = env.get_template(arguments['IN'])
        with open(arguments['OUT'], 'w') as out:
            out.write(template.render(**variables))


And the associated `Termite`_ task:

.. code-block:: yaml

    - shell:
        command: tcli render --input app/index.html --output build/index.html dev=true


In this example we are rendering a HTML template using `Jinja`_. To parse the command line arguments we are using `docopt`_.
