import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from typing import Optional
from metrics.page_counter import increment_page_counter, get_current_page_counter_value

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')

env_string: Optional[str] = None


@router.get('/')
def home(request: Request):
    increment_page_counter()
    hits = get_current_page_counter_value()
    return templates.TemplateResponse('home.html', {'request': request, 'env_string': env_string, 'page_hits': hits})
