#!/usr/bin/env python
# encoding: utf-8
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 17 Jun 18:31:35 CEST 2015

'''User script to conduct the first hypothesis in the course'''


import logging
import itertools

import numpy
numpy.seterr(divide='ignore')

import database
import preprocessor
import algorithm
import analysis


def test_one(protocol, variables):
  """Runs one single test, returns the CER on the test set"""

  # 1. get the data from our preset API for the database
  train = database.get(protocol, 'train', database.CLASSES, variables)

  # 2. preprocess the data using our module preprocessor
  norm = preprocessor.estimate_norm(numpy.vstack(train))
  train_normed = preprocessor.normalize(train, norm)

  # 3. trains our logistic regression system
  trainer = algorithm.MultiClassTrainer()
  machine = trainer.train(train_normed)

  # 4. applies the machine to predict on the 'unseen' test data
  test = database.get(protocol, 'test', database.CLASSES, variables)
  test_normed = preprocessor.normalize(test, norm)
  test_predictions = machine.predict(numpy.vstack(test_normed))
  test_labels = algorithm.make_labels(test).astype(int)
  return analysis.CER(test_predictions, test_labels)


def test_impact_of_variables_single(tabnum):
  """Builds the first table of my report"""

  for n, p in enumerate(database.PROTOCOLS):

    print "\nTable %d: Single variables for Protocol `%s`:" % \
      (n+tabnum, p)
    print 60*"-"

    for k in database.VARIABLES:
      result = test_one(p, [k])
      print ("%-15s" % k), "| %d%%" % (100 * result,)


def test_impact_of_variables_2by2(tabnum):
  """Builds the first table of my report"""

  for n, p in enumerate(database.PROTOCOLS):

    print "\nTable %d: Variable combinations, 2x2 for Protocol `%s`:" % \
      (n+tabnum, p)
    print 60*"-"

    for k in itertools.combinations(database.VARIABLES, 2):
      result = test_one(p, k)
      print ("%-30s" % ' + '.join(k)), "| %d%%" % (100 * result,)


def test_impact_of_variables_3by3(tabnum):
  """Builds the first table of my report"""

  for n, p in enumerate(database.PROTOCOLS):

    print "\nTable %d: Variable combinations, 3x3 for Protocol `%s`:" % \
            (n+tabnum, p)
    print 60*"-"

    for k in itertools.combinations(database.VARIABLES, 3):
      result = test_one(p, k)
      print ("%-45s" % ' + '.join(k)), "| %d%%" % (100 * result,)


def test_impact_of_variables_all(tabnum):
  """Builds the first table of my report"""

  for k, p in enumerate(database.PROTOCOLS):

    print "\nTable %d: All variables for Protocol `%s`:" % (k+tabnum, p)
    print 60*"-"

    result = test_one(p, database.VARIABLES)
    print ("%-45s" % ' + '.join(database.VARIABLES)), "| %d%%" % (100 * result,)


if __name__ == '__main__':

  print "Main script for Logistic Regression on Iris Flowers."
  test_impact_of_variables_single(1)
  test_impact_of_variables_2by2(3)
  test_impact_of_variables_3by3(5)
  test_impact_of_variables_all(7)
