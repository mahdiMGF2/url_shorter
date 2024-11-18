from fastapi import FastAPI, APIRouter,Request
from db.CURD.Link import AddLink,GetLink,DeleteLink
from fastapi.responses import RedirectResponse
import dotenv,os



dotenv.load_dotenv()
app = FastAPI(
    title="Url shorter",
    version="0.1",
    description="api for url shorter",
)

router = APIRouter()


@router.post("/AddUrl",tags=["Link shorter"])
async def AddUrl(url: str,request: Request):
    """
    param url\n
    return: id short url \n
    error code -1 : url already exists \n
    error code -2 : invalid url
    """
    StatusAdd = AddLink(url)
    print(request.client)
    if StatusAdd <= 0:
        return {"Error" : StatusAdd}
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
        return {"error" : StatusRemove}

app.include_router(router)