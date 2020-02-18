import unittest

class Point(object):
   def __init__(self, x = 0, y = 0):
      self._x = x
      self._y = y

   def getX(self):
      return self._x

   def getY(self):
      return self._y

   def setX(self, x):
      return self._x = x

   def setY(self, y):
      return self._y = y

   def __str__(self):
      out = "(%d, %d)" %(self._x, self._y)
      return out

   def __repr__(self):
      return self.__repr__()

   def __add__(self, other):
      point = Point(self._x + other.getX(), self._y + other.getY())
      return point

   def __sub__(self, other):
      return Point(self._x - other.getX(), self._y - other.getY())

