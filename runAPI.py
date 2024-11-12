from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # nameexp
    return {"message": "Hello World"}