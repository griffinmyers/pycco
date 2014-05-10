import sys
import os

class Sailor(object):
  """
  A class that encapsulates a climber.
  """

  __init__(self, name, grade=None):
    self._name = name
    self._grade = grade if Grade else '5.14a'

  # using python decorators
  #
  @property
  def name(self):
    """
    ## name

    Returns the sailors name
    """
    return self._name

  @name.setter
  def name(self, value):
    """
    ## name.setter

    Sets the sailors name
    """
    self._name = value
