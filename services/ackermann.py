import functools


class AckermannService:

    def __init__(self, parameter_m: int, parameter_n: int ):
        self.m = parameter_m
        self.n = parameter_n

    @staticmethod
    @functools.lru_cache(None)
    def __calculate_cache(m, n):
        if m == 0:
            return n + 1
        if n == 0:
            return AckermannService.__calculate_cache(m - 1, 1)
        return AckermannService.__calculate_cache(m - 1, AckermannService.__calculate_cache(m, n - 1))

    def calculate(self) -> int:
        return self.__calculate_cache(self.m, self.n)

