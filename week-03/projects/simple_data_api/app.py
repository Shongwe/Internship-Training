from fastapi import FastAPI
from routes import router

def create_app():
    app = FastAPI(title="Simple Data API")
    app.include_router(router, prefix="/api")
    return app

app = create_app()