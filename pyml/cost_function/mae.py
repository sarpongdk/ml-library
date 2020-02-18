class MeanAbsoluteError(AbstractCostFunction):
   def __init__(self):
      pass

   def score(self, true, predicted):
      super(true, predicted)

   def _scoreIter(self, true, predicted, coeff = 1):
      if (len(true) != len(predicted)):
         raise ValueError("The lengths of the input arguments should be the same")
      
      if coeff == 0:
         raise ValueError("Cannot have zero coefficient")

      n = len(true)
      score = 0
      for i in range(n):
         score += abs(true - predicted)
      return score/n

   def _scoreScalar(self, true, predicted):
      score = abs(true - predicted)


