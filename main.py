import uvicorn
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from routes import router
from src.config.config import Config
from src.middleware.timer import TimerMiddleware

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR if Config.ENV == 'development' else logging.WARNING)

if Config.ENV == 'development':
    handler = logging.FileHandler('errors.log')
    handler.setLevel(logging.ERROR)
else:
    handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

app.add_middleware(TimerMiddleware)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],     
    allow_methods=['*'], 
    allow_headers=['*']
)

""" NOTE: Middleware para capturar exceções """
@app.middleware('http')
async def log_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception:
        logger.error(f'Error without request: {request.method} {request.url}', exc_info=True)
        return JSONResponse(
            status_code=400,
            content={'detail': 'Internal Server Error'}
        )

app.mount('/tmp', StaticFiles(directory='tmp'), name='tmp')

@app.get('/health')
def health_check():
    return Config.PROJECT_INFO

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)