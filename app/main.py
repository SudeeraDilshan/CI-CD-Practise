from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD with FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/status")
def status():
    return {"status": "running", "version": "1.0.0"}

@app.get("/info")
def info():
    return {"app": "FastAPI CI/CD Demo", "version": "1.0.0", "description": "A simple FastAPI application for demonstrating CI/CD."}
