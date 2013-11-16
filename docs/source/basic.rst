================
 Basic concepts
================


.. include:: links.rst

Termite uses the `yaml`_  format to define commands and tasks. The wikipedia
has a `good description of the format <http://en.wikipedia.org/wiki/YAML>`_.

The mains entry point is a yaml file, called `termite.yaml`, Which should be in
your current working directory.

In termite we have two basic elements, the commands, and the tasks. A command
is a list of tasks, and should have a name, which is basically an identifier.
Let's see a basic `termite.yaml` file:

.. code-block:: yaml

    - command:
        name: dev
        tasks:
            - shell:
                command: echo "Hello world!!"

Run this in the command line to see the greeting:

.. code-block:: bash

    termite dev
