import logging
from json import JSONDecodeError

from starlette.requests import Request
from starlette.responses import JSONResponse

from services.fibonacci import FibonnaciService
from utils.response_generator import generate_response
from utils.system_messages import RECURSIVE_ERROR, INVALID_PAYLOAD, INVALID_PARAMETER_VALUE\



class FibonacciAction:

    @staticmethod
    async def fibonacci_action(request: Request) -> JSONResponse:
        try:
            request_body = await request.json()
            parameter_n = request_body['n']
            if parameter_n < 0:
                return generate_response(
                    message=[INVALID_PARAMETER_VALUE],
                    status_code=422
                )
            fibonacci_service = FibonnaciService(n=parameter_n)
            fibonacci_result = fibonacci_service.calculate()
            return generate_response(
                data={'result': fibonacci_result}
            )
        except RecursionError:
            return generate_response(
                message=[RECURSIVE_ERROR],
                status_code=500
            )

        except (JSONDecodeError, KeyError):
            return generate_response(
                message=[INVALID_PAYLOAD],
                status_code=400
            )
