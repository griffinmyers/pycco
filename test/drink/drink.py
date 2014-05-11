import sys
import os

class Seltzer(object):
  """
  A class that encapsulates a good beverage.
  """

  __init__(self, name, grade=None):
    self._name = name

  # using python decorators
  #
  @property
  def name(self):
    """
    ## name

    Returns the drinks name
    """
    return self._name

  @name.setter
  def name(self, value):
    """
    ## name.setter

    Sets the drinks name
    """
    self._name = value
