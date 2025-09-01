import time
from fastapi import Request, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = round(time.time() - start_time, 2)
        response.headers["X-Process-Time"] = str(process_time)

        return response