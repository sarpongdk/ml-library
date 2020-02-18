import math, unittest

class Euclidean(object):
   def __init__(self):
      pass

   def pythagoreanDistance(self, a, b):
      return math.sqrt( (a)**2 + (b)**2 )

   def getDistance(self, v1, v2):
      try:
         return self._vectorDistance(v1, v2)
      except TypeError:
         return self._pointDistance(v1, v2)

   def _vectorDistance(self, v1, v2):
      if len(v1) != len(v2):
         raise ValueError("Vectors should be of same length")

      distance = 0
      n = len(v1)
      for i in range(n):
         distance += (v1[i] - v2[i])**2
      return math.sqrt(distance)

   def _pointDistance(self, v1, v2):
      return math.sqrt( (v1.getX() - v2.getX())**2 + (v2.getY() - v2.getY())**2 )

