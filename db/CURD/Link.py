from db.Base import session
from db.models import Link
from  sqlalchemy.exc import SQLAlchemyError
import validators
def AddLink(link:str,Link = Link) -> int:
    if not  validators.url(link):
        return -2
    try:
        New_Link = Link(url=link)
        session.add(New_Link)
        session.commit()
        session.refresh(New_Link)
        return New_Link.id
    except SQLAlchemyError:
        session.rollback()
        return -1
    finally:
        session.close()


def GetLink(id:int,Link = Link) -> str:
    Link = session.query(Link).filter_by(id=id).first()
    if Link is None:return None
    return Link.url

def DeleteLink(id:int,Link = Link) -> int:
    try:
        deleted_rows = session.query(Link).filter_by(id=id).delete()
        session.commit()

        if deleted_rows == 0:
            return -1
        return 1
    except Exception:
        session.rollback()
        return -2
