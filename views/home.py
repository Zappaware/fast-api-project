import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader

from services import report_service

_env = Environment(loader=FileSystemLoader("templates"), cache_size=0)
templates = Jinja2Templates(env=_env)
router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    return templates.TemplateResponse(request, "home/index.html", {"events": events})


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
