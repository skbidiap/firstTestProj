#################################################################
Reproducible Logistic Regression on Fisher's Iris Flower Database
#################################################################

This bundle contains the code I used to generate the tables on the paper::

  @inproceedings{bob2012,
    author = {John Doe},
    title = {A Simple Solution to Iris Flower Classification},
    year = {2015},
    month = jun,
    booktitle = {Reproducible Research Conference, Rio de Janeiro, 2015},
    url = {http://example.com/path/to/my/article.pdf},
  }


We appreciate your citation in case you use results obtained directly or
indirectly via this software package.


Installation
------------

This package depends on `numpy <http://www.numpy.org>`_ and `scipy
<http://www.scipy.org>`_ to run properly. Please install a modern version of
these packages before trying to run the code examples.

The tests on my paper were executed on a machine running Xubuntu 14.04.2
installation with Python 2.7.


Running
-------

I have created a script that can run the source code reproducing all tables
from the above paper. Run it like so::

  $ python ./paper.py

The contents of each table in the paper should be printed one after the other.


Troubleshooting
---------------

You can run unit tests I have prepared like this::

  $ nosetests ./test.py

In case of problems, please get in touch with me `by e-mail
<mailto:john.doe@example.com>`_.

Licensing
---------

This work is licensed under the GPLv3_.


.. Here goes our links
.. _GPLv3: http://www.gnu.org/licenses/gpl-3.0.en.html
