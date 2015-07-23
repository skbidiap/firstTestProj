#!/usr/bin/env python
# encoding: utf-8
# Andre Anjos <andre.anjos@idiap.ch>
# Fri 19 Jun 17:49:18 2015 CEST

'''Database specifications for an evaluation protocol based on the Iris Flower
databases from Fisher's original work.'''


import numpy


# A list of protocols we implement
PROTOCOLS = {
        'proto1': {'train': xrange(0, 30), 'test': xrange(30, 50)},
        'proto2': {'train': xrange(20, 50), 'test': xrange(0, 20)},
        }

# Subsets of the database in each protocol
SUBSETS = [
        'train',
        'test',
        ]

# The types of Iris flowers in the dataset
CLASSES = [
        'setosa',
        'versicolor',
        'virginica',
        ]

# The four values that were sampled
VARIABLES = [
        'sepal length',
        'sepal width',
        'petal length',
        'petal width',
        ]


def load():
  '''Loads the data from its CSV format into an easy to dictionary of arrays'''

  import csv
  data = dict([(k,[]) for k in CLASSES])
  with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for k, row in enumerate(reader):
      if not k: continue
      data[row[4]].append(numpy.array([float(z) for z in row[:4]]))
  for k in CLASSES:
    data[k] = numpy.vstack(data[k])
  return data


def split_data(data, subset, splits):
  '''Returns the data for a given protocol
  '''

  return dict([(k, data[k][splits[subset]]) for k in data])


def get(protocol, subset, classes=CLASSES, variables=VARIABLES):
  '''Returns the data subset given a particular protocol


  Parameters

    protocol (string): one of the valid protocols supported by this interface

    subset (string): one of 'train' or 'test'

    classes (list of string): a list of strings containing the names of the
      classes from which you want to have the data from

    variables (list of strings): a list of strings containg the names of the
      variables (features) you want to have data from


  Returns:

    data (numpy.ndarray): The data for all the classes and variables nicely
      packed into one numpy 3D array. One depth represents the data for one
      class, one row is one example, one column a given feature.

  '''

  retval = split_data(load(), subset, PROTOCOLS[protocol])

  # filter variables (features)
  varindex = [VARIABLES.index(k) for k in variables]

  # filter class names and variable indexes at the same time
  retval = dict([(k, retval[k][:,varindex]) for k in classes])

  # squash the data
  return numpy.array([retval[k] for k in classes])
