from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # name
    return {"message": "Hello World"}