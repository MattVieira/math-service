import functools


class FactorialService:

    def __init__(self, n: int):
        self.n = n

    @staticmethod
    @functools.lru_cache(None)
    def __calculate_cache(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * FactorialService.__calculate_cache(n - 1)

    def calculate(self) -> int:
        return self.__calculate_cache(self.n)
