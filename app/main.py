from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD with FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
