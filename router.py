"""
Router fo the Math Service Application
"""
from starlette.routing import Route

from actions.ackermann import AckermannAction
from actions.fibonacci import FibonacciAction
from actions.factorial import FactorialAction

BASE_PATH = '/math/v1'


class Router:
    """
    Class that will manage all application routes
    """

    @staticmethod
    def get_routes() -> list:
        """
        Format and return all routes
        :return: list
        """
        return [
            Route(f'{BASE_PATH}/fibonacci',
                  FibonacciAction().fibonacci_action,
                  methods=["POST"]),
            Route(f'{BASE_PATH}/ackermann',
                  AckermannAction().ackermann_action,
                  methods=["POST"]),
            Route(f'{BASE_PATH}/factorial',
                  FactorialAction().factorial_action,
                  methods=["POST"]),
        ]
