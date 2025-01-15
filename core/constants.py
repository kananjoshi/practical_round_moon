from enum import Enum


class Species(Enum):
  DOG = 'dog'
  CAT = 'cat'

class AdoptionStatus(Enum):
    PENDING = 0
    ADOPTED =  1
    REJECTED = 2

class HealthStatus(Enum):
    GOOD = "Good"
    BAD = "Bad"
