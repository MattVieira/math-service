from json import JSONDecodeError

from starlette.requests import Request
from starlette.responses import JSONResponse

from services.ackermann import AckermannService
from utils.response_generator import generate_response
from utils.system_messages import RECURSIVE_ERROR, INVALID_PAYLOAD, INVALID_PARAMETER_VALUE


class AckermannAction:

    @staticmethod
    async def ackermann_action(request: Request) -> JSONResponse:
        try:
            request_body = await request.json()
            parameter_n, parameter_m = request_body['n'], request_body['m']
            if parameter_n < 0 or parameter_m < 0:
                return generate_response(
                    message=[INVALID_PARAMETER_VALUE],
                    status_code=422
                )
            ackermann_service = AckermannService(parameter_m, parameter_n)
            ackermann_result = ackermann_service.calculate()
            return generate_response(
                data={
                    'result': ackermann_result
                }
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

