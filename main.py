from fastapi import FastAPI
import subprocess
import os

app = FastAPI(title="Nexus Pendant Laptop Agent")


@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Nexus Laptop Agent"
    }


@app.post("/open_chrome")
def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    return {"message": "Chrome opened"}


@app.post("/open_vscode")
def open_vscode():
    subprocess.Popen("code", shell=True)
    return {"message": "VS Code opened"}


@app.post("/lock")
def lock_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return {"message": "PC locked"}