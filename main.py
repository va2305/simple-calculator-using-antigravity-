from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/sum")
async def sum(a: float, b: float):
    return {"result": a + b}

@app.get("/sub")
async def sub(a: float, b: float):
    return {"result": a - b}

@app.get("/mul")
async def mul(a: float, b: float):
    return {"result": a * b}

@app.get("/div")
async def div(a: float, b: float):
    if b == 0:
        return {"result": "Error: Division by zero"}
    return {"result": a / b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
