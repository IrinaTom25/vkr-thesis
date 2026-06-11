from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.dependencies import init_dependencies
from app.routes import config_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    deps = init_dependencies()
    print("Dependencies initialized:", list(deps.keys()))
    yield
    print("Application shutdown")


app = FastAPI(
    title="Laboratory FastAPI App",
    version="1.0.0",
    description="Educational application for lab 6",
    lifespan=lifespan,
)

app.include_router(config_routes.router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/ping")
async def ping():
    return "pong"