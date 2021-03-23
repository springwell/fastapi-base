import uvicorn
from fastapi import FastAPI
from .routers import users

app = FastAPI()

app.include_router(users.router)


@app.get("/", response_model=str)
def it_works():
    # it works
    return "it works!"


if __name__ == '__main__':
    uvicorn.run(app)
