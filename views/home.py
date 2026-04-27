import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from jinja2 import Environment, FileSystemLoader
_env = Environment(loader=FileSystemLoader("templates"), cache_size=0)
templates = Jinja2Templates(env=_env)
router = fastapi.APIRouter()


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "home/index.html")


@router.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
