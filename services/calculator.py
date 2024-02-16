import random


class RandomRepository:

  def __init__(self) -> None:
    pass

  def one_to_three(self):
    return random.randint(1, 3)


class CalculatorService:

    def __init__(self, random_repo: RandomRepository) -> None:
      self.random_repo = random_repo

    def add(self, x: int, y: int):
      return float(x + y)

    def random_with_constant(self, constant: int):
      return constant + self.random_repo.one_to_three()
