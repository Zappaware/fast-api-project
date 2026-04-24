import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/api/calculate")
def calculate():
    value = 2 + 2

    result = {"value": value}
    return result


uvicorn.run(api)
