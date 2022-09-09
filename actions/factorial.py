from json import JSONDecodeError

from starlette.requests import Request
from starlette.responses import JSONResponse

from services.factorial import FactorialService
from utils.response_generator import generate_response
from utils.system_messages import RECURSIVE_ERROR, INVALID_PAYLOAD, INVALID_PARAMETER_VALUE


class FactorialAction:

    @staticmethod
    async def factorial_action(request: Request) -> JSONResponse:
        try:
            request_body = await request.json()
            parameter_n = request_body['n']
            if parameter_n < 0:
                return generate_response(
                    message=[INVALID_PARAMETER_VALUE],
                    status_code=422
                )
            factorial_service = FactorialService(n=parameter_n)
            factorial_result = factorial_service.calculate()
            return generate_response(
                data={'result': factorial_result}
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
