from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()


templates = Jinja2Templates(directory='templates')


@router.get('/')
async def index_page_handler(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index/index.html'
    )
