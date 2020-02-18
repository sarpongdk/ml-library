import math, unittest

class Vector(object):
   def __init__(self, vector = None, length = 2):
      self._length = len(vector) if vector else length
      self._vector = vector if vector else [0] * length
   
   def __add__(self, other):
      if len(other) != self._length:
         raise ValueError("Cannot add vectors of different lengths")

      newVector = [0] * self._length
      for i in range(self._length):
         newVector[i] = other.get(i) + self._vector[i]

      return newVector

   def __getitem__(self, index):
      return self._vector[index]

   def __eq__(self, other):
      if len(other) != self._length:
         return False
      for i in range(self._length):
         if self._vector[i] != other.get(i):
            return False
      return True

   def __lt__(self, other):
      """
      Return false if any term is greater than or equal to the other vector
      """
      for i in range(self._length):
         if self._vector[i] >= other.get(i):
            return False
      return True

   def __le__(self, other):
      return self.__eq__(other) or self.__lt__(other)

   def __len__(self):
      return self._length

   def __sub__(self, other):
      if len(other) != self._length:
         raise ValueError("Cannot subtract vectors of different lengths")

      newVector = [0] * self._length
      for i in range(self._length):
         newVector[i] = other.get(i) - self._vector[i]

      return newVector

   def __mul__(self, multiplier):
      """
      If scalar is provided, returns standard vector multiplication with scalar
      If vector is provided, dot product of the two vectors is returned
      For cross product, use crossProduct() method
      """
      if isinstance(multiplier, (int, float)):
         return self._scalarMultiply(scalar)
      else:
         return self.dotProduct(multiplier)

   def _scalarMultiply(self, scalar):
      newVector = [0] * self._length
      for i in range(self._length):
         newVector[i] = scalar * self._vector[i]
      return newVector

   def _divide(self, scalar):
      if isinstance(multiplier, (int, float)):
         return self._scalarMultiply(1/scalar)
      else:
         raise TypeError("Vector division is only possible with scalars")

   def __floordiv__(self, other):
      self._divide(other)

   def __truediv__(self, other):
      self._divide(other)

   def addTerm(self, term):
      self._length += 1
      self._vector.append(term)

   def getMagnitude(self):
      magnitude = 0
      for term in self._vector:
         magnitude += term**2
      return math.sqrt(magnitude)

   def getUnitVector(self):
      newVector = [0] * self._length
      magnitude = self.getMagnitude()
      for i in range(self._length):
         newVector[i] = self._vector[i] / magnitude
      return newVector

   def dotProduct(self, vector):
      if len(vector) != self._length:
         raise ValueError("Cannot multiply vectors of different length")
      newVector = [0] * self._length
      for i in range(self._length):
         newVector[i] = self._vector[i] * vector[i]
      return newVector

   def get(self, index):
      return self._vector[index]

   def crossProduct(self, vector):
      pass

   def cosineSimilarity(self, vector):
      pass

   def __str__(self):
      out = "["
      for i in range(self._length):
         out += str(self._vector[i])
         if (i < self._length - 1):
            out += ","
      out += "]"
      return out

   def __repr__(self):
      return self.__str__()
