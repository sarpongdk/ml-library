from abc import ABC, abstractmethod

import unittest

class AbstractCostFunction(ABC):
   def __init__(self):
      pass

   def score(true, predicted):
      try:
         return _scoreIter(true, predicted)
      except TypeError:
         return _scoreScalar(true, predicted)

   @abstractmethod
   def _scoreIter(true, predicted):
      pass

   @abstractmethod
   def _scoreScalar(true, predicted):
      pass

   def __str__(self):
      return "Abstract Cost Function"


class TestAbstractCostFunction(unittest.TestCase):
   def test_abstractConstructor(self):
      self.assertRaises(TypeError, AbstractCostFunction)

if __name__ == "__main__":
   unittest.main()
