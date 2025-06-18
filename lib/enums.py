from enum import Enum

class Operators(Enum):
   addition = "+"
   subtraction = "-"
   multiplication = "*"
   devision = "/"
   power = "^"

   def __repr__(self):
      return self.__str__()

   def __str__(self):
      return self.value