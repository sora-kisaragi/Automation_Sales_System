from fastapi import FastAPI
from routers import router1, router2

app = FastAPI()

app.include_router(router1.router)
app.include_router(router2.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)