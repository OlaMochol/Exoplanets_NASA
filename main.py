from fastapi import FastAPI

api = FastAPI()

@api.get("/planets")
def planets():
    return "hello"