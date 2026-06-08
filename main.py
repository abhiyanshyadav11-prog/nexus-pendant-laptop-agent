from fastapi import FastAPI
from pydantic import BaseModel

from app.services.app_launcher import launch_app

app = FastAPI(title="Nexus Pendant Laptop Agent")


class AppRequest(BaseModel):
    app_name: str


@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Nexus Laptop Agent"
    }


@app.post("/open_app")
def open_app(request: AppRequest):

    success = launch_app(request.app_name)

    if success:
        return {
            "status": "success",
            "app": request.app_name
        }

    return {
        "status": "error",
        "message": "App not supported"
    }