from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def root():
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)