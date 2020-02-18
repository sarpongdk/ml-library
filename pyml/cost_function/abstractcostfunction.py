from abc import ABC, abstractmethod

import unittest

class AbstractCostFunction(ABC):
   def __init__(self):
      pass

   def score(self, true, predicted):
      try:
         return self._scoreIter(true, predicted)
      except TypeError:
         return self._scoreScalar(true, predicted)

   @abstractmethod
   def _scoreIter(self, true, predicted):
      pass

   @abstractmethod
   def _scoreScalar(self, true, predicted):
      pass

   def __str__(self):
      return "Abstract Cost Function"


class TestAbstractCostFunction(unittest.TestCase):
   def test_abstractConstructor(self):
      self.assertRaises(TypeError, AbstractCostFunction)

if __name__ == "__main__":
   unittest.main()
