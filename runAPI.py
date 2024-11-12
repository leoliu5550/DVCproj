from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # name2
    return {"message": "Hello World"}