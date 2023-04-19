from fastapi import FastAPI
import uvicorn
from apis.routers import init_apis
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_apis(app)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8086, reload=True)

