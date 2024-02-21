from app.repositories.random import RandomRepository
from app.utils.log import log


class CalculatorService:
    def __init__(self, random_repo: RandomRepository) -> None:
        self.random_repo = random_repo

    @log
    def add(self, x: int, y: int):
        return float(x + y)

    @log
    def random_with_constant(self, constant: int):
        return constant + self.random_repo.one_to_three()
