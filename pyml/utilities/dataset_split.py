from abc import ABC, abstractmethod

class DatasetSplit(ABC):
   def __init__(self):
      pass

   @abstractmethod
   def split(data, ratio):
      pass


