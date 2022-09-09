import functools


class FibonnaciService:
    """
        I created a service class with statistical methods to demonstrate how easy it would be to change the business
        logic internally without changing the code of the action that will only take care of the request
    """

    def __init__(self, n: int):
        self.n = n

    @staticmethod
    @functools.lru_cache(None)
    def __calculate_cache(n: int) -> int:
        if n < 2:
            return n
        return FibonnaciService.__calculate_cache(n - 1) + FibonnaciService.__calculate_cache(n - 2)

    @staticmethod
    def __calculate_memoization(n: int, computed={0: 0, 1: 1}) -> int:
        if n not in computed:
            computed[n] = FibonnaciService.__calculate_memoization(n - 1, computed) + \
                          FibonnaciService.__calculate_memoization(n - 2, computed)
        return computed[n]

    def calculate(self) -> int:
        return self.__calculate_memoization(self.n) if self.n >= 250 else self.__calculate_cache(self.n)
