from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/Summation")
async def Summation(a: float, b: float):
    print("Expected JSON response")
    return {"sum": a + b}
    