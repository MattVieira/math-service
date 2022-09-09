from starlette.responses import JSONResponse


def generate_response(data: dict = {}, message: list = [], status_code: int = 200, notice: list = []):
    """HTTP response pattern design function
    | default status code is 200
    | default notice arg  is an empty list"""

    return JSONResponse({
        "message": message,
        "notice": notice,
        "data": data,
    }, status_code=status_code)