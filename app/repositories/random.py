import random
from app.utils.log import log


class RandomRepository:
    def __init__(self) -> None:
        pass

    @log
    def one_to_three(self):
        return random.randint(1, 3)
