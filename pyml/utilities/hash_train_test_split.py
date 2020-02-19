import random

class HashTrainTestSplit(DatasetSplit):
   def __init__(self):
      pass

   def _split(data, ratio):
      """
      Returns two matrices from the provided matrix, split according to the specified ratio.
      """
      shuffled = random.shuffle(data)
      trainSize = int(len(shuffled) * ratio)
      train = shuffled[:trainSize + 1]
      test = shuffled[trainSize + 1:]
      return (train, test)
      
