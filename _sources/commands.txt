.. include:: links.rst

==========
 Commands
==========

Commands define the tasks to be run. An example of a `termite.yaml` file with 2
commands:

.. code-block:: yaml

    - command:
        name: hello
        tasks:
            - shell:
                command: echo "Hello world!!"

    - command:
        name: bye
        tasks:
            - shell:
                command: echo "Goodbye!!"


Pass the name of the command to termite as its first argument. If you don't
specify any command name in the command line, `Termite`_ runs the first command
found. In this example, running in the command line:

.. code-block:: bash

    termite hello

has the same effect as run just

.. code-block:: bash

    termite


Global tasks
------------

It is possible create a task globally and use it in several commands, an example:


.. code-block:: yaml

    - shell: &some_id
        command: echo "Hello world!!"

    - command:
        name: hello
        tasks:
            - shell: *some_id

    - command:
        name: bye
        tasks:
            - shell: *some_id

            - shell:
                command: echo "Goodbye!!"
