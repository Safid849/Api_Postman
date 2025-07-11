from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
def read_hello(request: Request, name: str = None, is_teacher: bool = None):
    accept_headers = request.headers.get("Accept")

    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)
    return JSONResponse(content="Hello World", status_code=200)


class WelcomeRequest(BaseModel):
    name: str


@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {"message": f"Bienvenue {request.name}"}
