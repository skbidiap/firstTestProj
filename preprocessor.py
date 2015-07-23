#!/usr/bin/env python
# encoding: utf-8
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 18 Jun 14:24:51 CEST 2015

'''A simple pre-processing that applies Z-normalization to the input
features'''


import numpy


def estimate_norm(X):
  '''Estimates the mean and standard deviation from a data set


  Parameters:

    X (numpy.ndarray): A 2D numpy ndarray in which the rows represent examples
      while the columns, features of the data you want to estimate
      normalization parameters on


  Returns:

    numpy.ndarray: A 1D numpy ndarray containing the estimated mean over
      dimension 1 (columns) of the input data X

    numpy.ndarray: A 1D numpy ndarray containing the estimated unbiased
      standard deviation over dimension 1 (columns) of the input data X

  '''

  return X.mean(axis=0), X.std(axis=0, ddof=1)


def normalize(X, norm):
  '''Applies the given norm to the input data set


  Parameters:

    X (numpy.ndarray): A 3D numpy ndarray in which the rows represent examples
      while the columns, features of the data set you want to normalize. Every
      depth corresponds to data for a particular class

    norm (tuple): A tuple containing two 1D numpy ndarrays corresponding to the
      normalization parameters extracted with :py:func:`estimated_norm` above.


   Returns:

     numpy.ndarray: A 3D numpy ndarray with the same dimensions as the input
       array ``X``, but with its values normalized according to the norm input.

  '''

  return numpy.array([(k - norm[0]) / norm[1] for k in X])
