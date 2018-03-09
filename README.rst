==========
LED TESTER
==========


.. image:: https://img.shields.io/pypi/v/led_tester.svg
        :target: https://pypi.python.org/pypi/led_tester

.. image:: https://img.shields.io/travis/harshrpg/led_tester.svg
        :target: https://travis-ci.org/harshrpg/led_tester

.. image:: https://readthedocs.org/projects/led-tester/badge/?version=latest
        :target: https://led-tester.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Testing an array of LEDs


* Free software: MIT license
* Documentation: https://led-tester.readthedocs.io.


Features
--------

This is an assignment that is used to test LEDs that are assumed to be a part of a grid. It accepts command line arguments as inputs:
    
    ``--input`` or ``-i`` to tell the program that next argument is an input
    
    ``<File Path>`` This can be local file path or a network URI

Installation
-------------

Run the below command to install this project::
    
    $ pip install git+https://github.com/harshrpg/COMP30670_LedTester.git

Usage
-----

Run the below command to use this project::

    $ solve_led --input <file>
    
Replace ``<file>`` with the path of the file

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
