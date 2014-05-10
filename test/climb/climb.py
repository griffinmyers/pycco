import sys
import os

class Climber(object):
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

    Returns the climbers name
    """
    return self._name

  @name.setter
  def name(self, value):
    """
    ## name.setter

    Sets the climbers name
    """
    self._name = value
