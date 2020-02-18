from mse import MeanSquareError

class RootMeanSquareError(MeanSquareError):
   def __init__(self):
      pass

   def score(self, true, predicted):
      super(true, predicted)

   def _scoreIter(self, true, predicted, coeff = 1):
      score = super()._scoreIter(true, predicted, coeff)
      return sqrt(score)

   def _scoreScalar(self, true, predicted):
      score = super()._scoreScalar(true, predicted)
      return sqrt(score)


