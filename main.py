from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
def read_hello(request: Request, name: str = None, is_teacher: bool = False):
    accept_headers = request.headers.get("Accept")

    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)

    if name and is_teacher:
        return JSONResponse({"message": f"Hello Teacher {name}!"}, status_code=200)
    elif name is None and is_teacher:
        return JSONResponse({"message": "Hello Teacher non défini !"}, status_code=200)
    elif name is None and is_teacher is None:
        return JSONResponse({"message": "Hello World"}, status_code=200)
    else:
        return JSONResponse({"message": f"Hello {name}"}, status_code=200)


@app.put("/top-secret")
def top_secret(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        return JSONResponse(
            {
                "error": "Forbidden",
                "detail": "No key provided."
            },
            status_code=403
        )
    if auth_header != "Zinedis_secret-key":
        return JSONResponse({"error": "Forbbiden", "Provide_key": auth_header}, status_code=403)

    return JSONResponse({"message": "Welcome, authentication succeeded!"}, status_code=200)


class WelcomeRequest(BaseModel):
    name: str


@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {"message": f"Bienvenue {request.name}"}
