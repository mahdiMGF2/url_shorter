from fastapi import FastAPI, APIRouter,Request
from fastapi.openapi.utils import status_code_ranges
from fastapi.responses import RedirectResponse,HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

from db.CURD.Link import AddLink,GetLink,DeleteLink
import dotenv,os



dotenv.load_dotenv()
app = FastAPI(
    title="Url shorter",
    version="0.1",
    description="api for url shorter",
)
templates = Jinja2Templates(directory="templates/")
router = APIRouter()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/AddUrl",tags=["Link shorter"])
async def AddUrl(url: str,request: Request):
    """
    param url\n
    return: id short url \n
    error code -1 : url already exists \n
    error code -2 : invalid url
    """
    StatusAdd = AddLink(url)
    if StatusAdd <= 0:
        return JSONResponse(status_code=500,content={"Error" : StatusAdd})
    else:
        return {"url" : f"{os.getenv('URLBALSE')}url/{StatusAdd}"}


@router.get("/url/{id}",tags=["Link shorter"])
def GetUrl(id:int):
    """
        param id url\n
        return: Redirect url \n
        """
    url = GetLink(id)
    if url is None:
        return {"url" : None}
    return RedirectResponse(url)


@router.delete("/delete_url/{id}",tags=["Link shorter"])
def DeleteUrl(id:int):
    """
        param url\n
        return: id short url \n
        error code -1 : not found \n
        """
    StatusRemove = DeleteLink(id)
    if StatusRemove == 1:
        return {"url" : "ok!"}
    else:
        return JSONResponse(status_code=500,content={"Error" : StatusRemove})

app.include_router(router)