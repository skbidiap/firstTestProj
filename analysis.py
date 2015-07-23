#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 17 Jun 2015 18:14:13 CEST

def CER(prediction, true_labels):
  """
  Calculates the classification error rate for an N-class classification problem


  Parameters:

  prediction (numpy.ndarray): A 1D :py:class:`numpy.ndarray` containing your
    prediction

  true_labels (numpy.ndarray): A 1D :py:class:`numpy.ndarray`
    containing the ground truth labels for the input array, organized in the
    same order.

  """

  errors = (prediction != true_labels).sum()
  return float(errors)/len(prediction)
