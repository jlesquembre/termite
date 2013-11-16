
=====
Tasks
=====

.. include:: links.rst

There are 3 types of tasks in `Termite`_, `shell`, `cp` and `server`


Shell tasks
~~~~~~~~~~~

Shell tasks accepts 3 options, :ref:`command`, :ref:`cwd` and :ref:`watch
<shell-watch>`.



.. _command:

Command (Mandatory)
^^^^^^^^^^^^^^^^^^^

Specifies the command to run. Is also possible specify a list of commands. In
this case, the commands are run sequentially.


.. _cwd:

Cwd (Optional)
^^^^^^^^^^^^^^

The current directory will be changed to `cwd` before the command is executed.


.. _shell-watch:

Watch (Optional)
^^^^^^^^^^^^^^^^

List of files to watch for modifications. After any change, the command is
executed again. It is possible to use shell-style wildcards (`*` or `**`). It
is also possible specify folders to watch, in this case `/some/path/` and
`/some/path/**` have the same effect.
If watch is omitted, the command is run only once.



Cp tasks
~~~~~~~~

Copy files is a very common operation, thats the reason have a task for this
operation, although would we possible to use a command task for copy files. For
`cp` tasks there are 3 options, :ref:`source`, :ref:`dest` and :ref:`watch
<cp-watch>`.


.. _source:

Source (Mandatory)
^^^^^^^^^^^^^^^^^^

A file, or list of files to copy. Shell-style wildcards are allowed.


.. _dest:

Dest (Mandatory)
^^^^^^^^^^^^^^^^

Where copy the file or files. Should be a folder, if doesn't exist is created.
Be careful, files are overwritten without any warning.


.. _cp-watch:

Watch (Optional)
^^^^^^^^^^^^^^^^

Specifies if the source files should be monitored. It is boolean value, by
default the value is set to `False`.



Server task
~~~~~~~~~~~

This task start an HTTP server. If you are watching any files, your browser is
automatically refreshed after every change. Has only one option, :ref:`path`.

.. _path:

Path (Mandatory)
^^^^^^^^^^^^^^^^

Serves files from this directory.


